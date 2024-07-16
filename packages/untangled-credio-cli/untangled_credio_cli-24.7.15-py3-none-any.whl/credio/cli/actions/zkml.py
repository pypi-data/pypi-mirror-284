import asyncio
import json
import subprocess
import sys
import time
from typing import List
import rich
import rich.live
import rich.progress
import rich.text
import typer

from credio.cli.actions.artifact import Artifact
from credio.cli.actions.config import (
    DEFAULT_SSH_CLIENT_PRIVATE_KEY_PATH,
    DEFAULT_SSH_CLIENT_PUBLIC_KEY_PATH,
)
from credio.cli.actions.proxy import Endpoint, start_proxy


action = typer.Typer()


@action.command(name="tool", help="Use ezkl tool with a specific ML model.")
def use_tool(command: str):
    args = sys.argv[3:]
    if command == "help":
        subprocess.run(["ezkl", "--help"])
    elif command == "install":  # TODO: Fetch installation binary from GitHub releases
        for _ in rich.progress.track(range(3600), description="Installing ezkl..."):
            time.sleep(1)
        rich.print("[red]Installation failed.[/red]")
    elif len(args) > 0:
        subprocess.run(["ezkl", command, *args])
    else:
        subprocess.run(["ezkl", command, "--help"])


@action.command(
    name="submit",
    help="Submit a specific challenge-accepted ML model's artifact to Credio platform.",
)
def submit_model(
    challenge: int,
    circuit: str = "model.compiled",
    settings: str = "settings.json",
    more: List[str] = [],
):
    files = [circuit, settings, *more]
    res = asyncio.run(Artifact().upload(*files, type="model", challenge=challenge))
    rich.print("[green]Uploaded.[/green]")
    rich.print_json(json=json.dumps(res))


@action.command(
    name="register", help="Register an endpoint for serving a specific ML model."
)
def register_endpoint(
    model_id: int, public_key_path: str = DEFAULT_SSH_CLIENT_PUBLIC_KEY_PATH
):
    rich.print(
        asyncio.run(
            Endpoint().register(model_id=model_id, public_key_path=public_key_path)
        )
    )


@action.command(
    name="list", help="List all registered endpoints for serving ML models."
)
def list_endpoints():
    rich.print_json(json.dumps(asyncio.run(Endpoint().list_all())))


@action.command(
    name="serve",
    help="Start serving a specific ML model (tunnelly connect to Credio platform).",
)
def serve(
    model_id: int,
    port: int = 8080,
    private_key: str = DEFAULT_SSH_CLIENT_PRIVATE_KEY_PATH,
    autoconnect: bool = True,
):
    remote_port = asyncio.run(Endpoint().get_assigned_port(model_id=model_id))
    start = lambda: start_proxy(
        model_id=model_id,
        remote_port=remote_port,
        local_port=port,
        private_key_path=private_key,
    )
    wait = 5  # seconds
    while True:
        start()
        if autoconnect:
            text = rich.text.Text(text="Reconnecting...")
            with rich.live.Live(text):
                for i in range(wait + 1):
                    time.sleep(1)
                    text._text = [
                        (
                            "Reconnecting..."
                            if i == wait
                            else "Reconnecting %s..." % (wait - i)
                        )
                    ]
