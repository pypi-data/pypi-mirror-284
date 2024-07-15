import asyncio
import json
import logging
import logging.config
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Optional
from uuid import UUID

import click
from prettytable import PrettyTable
from requests import ConnectionError, HTTPError
from tqdm import tqdm
from xpipe_client import AsyncClient, Client

logger = logging.getLogger(__name__)


# Resolving to shortest name length for now, probably want to throw an error on duplicates once testing is done
def resolve_connection_name(client: Client, name: str, con_type: str = '*') -> Optional[str]:
    # If the name is a valid UUID, assume we want to just use it without trying to look anything up
    try:
        UUID(name)
        return name
    except ValueError:
        pass

    all_connections = client.get_connections(types=con_type)
    possible_matches = sorted(
        [x for x in all_connections if x["name"] and x["name"][-1] == name], key=lambda x: len(x["name"])
    )
    return possible_matches[0]["connection"] if possible_matches else None


XPIPE_DEFAULT_LOCATIONS = {
    "win32": (
        os.path.join(os.getenv("LOCALAPPDATA", ""), "XPipe", "cli", "bin", "xpipe.exe"),
        os.path.join(os.getenv("LOCALAPPDATA", ""), "XPipe PTB", "cli", "bin", "xpipe.exe"),
    ),
    "cygwin": (
        os.path.join(os.getenv("LOCALAPPDATA", ""), "XPipe", "cli", "bin", "xpipe.exe"),
        os.path.join(os.getenv("LOCALAPPDATA", ""), "XPipe PTB", "cli", "bin", "xpipe.exe"),
    ),
    "linux": ("/opt/xpipe/cli/bin/xpipe", "/opt/xpipe-ptb/cli/bin/xpipe"),
    "darwin": ("/Applications/XPipe.app/Contents/MacOS/xpipe", "/Applications/XPipe PTB.app/Contents/MacOS/xpipe"),
}


def start_xpipe(ptb: bool = False, custom_install: Optional[str] = None) -> bool:
    if custom_install:
        full_path = Path(custom_install)
    else:
        pathstr = shutil.which("xpipe-ptb" if ptb else "xpipe")
        if not pathstr:
            pathstr = XPIPE_DEFAULT_LOCATIONS.get(sys.platform, (None, None))[ptb]
        if not pathstr:
            return False
        full_path = Path(pathstr)
    if not full_path.exists():
        return False
    success = subprocess.call([full_path, "daemon", "start"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return success == 0


@click.group()
@click.option("--ptb", is_flag=True, help="Use PTB port instead of release port")
@click.option("--base-url", default=None, help="Override the URL of the XPipe server to talk to")
@click.option("--token", default=None, help="The API token to use if the XPipe server isn't local")
@click.option("--debug", is_flag=True, help="Turn on xpipe_client debug logging")
@click.option("--start-if-needed", is_flag=True, help="Attempt to start the XPipe daemon if unable to connect")
@click.option("--custom-xpipe-location", default=None, help="Use a custom XPipe location with --start-if-needed")
@click.version_option()
@click.pass_context
def cli(
    ctx: click.Context,
    ptb: bool,
    base_url: Optional[str],
    token: Optional[str],
    debug: bool,
    start_if_needed: bool,
    custom_xpipe_location: Optional[str],
):
    if start_if_needed:
        # This is a no-op if the daemon is already running
        start_xpipe(ptb, custom_xpipe_location)
    ctx.obj = Client(token=token, base_url=base_url, ptb=ptb)
    if debug:
        # Otherwise, urllib3 spams on every connection if it's set to debug
        logging.getLogger("urllib3").propagate = False
        logging.basicConfig(level=logging.DEBUG)

    try:
        ctx.obj.renew_session()
    except ConnectionError:
        print(
            f"Failed to connect to {ctx.obj.base_url}. \n"
            "Check if XPipe is running, and if you're running the PTB version of XPipe, "
            "try passing the --ptb flag before your action, like so: \n"
            "xpipe-cli --ptb ls"
        )
        exit(1)


@cli.command()
@click.option("--category", "-c", default="*", help="Globbed category filter, defaults to *")
@click.option("--name", "-n", default="*", help="Globbed name filter, defaults to *")
@click.option("--type", default="*", help="Globbed type filter, defaults to *")
@click.option(
    "--output-format",
    "-f",
    default="text",
    type=click.Choice(["text", "html", "json", "csv", "latex"]),
    help="Output format",
)
@click.option(
    "--sort-by",
    default="name",
    type=click.Choice(["name", "type", "category", "uuid"], case_sensitive=False),
    help="Field to sort by",
)
@click.option("--reverse", is_flag=True, help="Sort the table in reverse")
@click.pass_obj
def ls(client: Client, category: str, name: str, type: str, output_format: str, sort_by: str, reverse: bool):
    """List connections, with optional filters"""
    connections = client.get_connections(categories=category, connections=name, types=type.lower())
    table = PrettyTable()
    table.align = "l"
    table.field_names = ["Name", "Type", "Category", "UUID"]
    for c in connections:
        table.add_row(["/".join(c["name"]), c["type"], ",".join(c["category"]), c["connection"]])
    print(table.get_formatted_string(output_format, sortby=sort_by.title(), reversesort=reverse))


async def probe_connections(async_client: AsyncClient, connections: List[dict]) -> bool:
    lock = asyncio.Semaphore(10)

    async def _probe(connection: dict) -> dict:
        async with lock:
            try:
                return await async_client.shell_start(connection["connection"])
            except Exception as e:
                print(f"Connection '{'/'.join(connection['name'])}' failed with error {e}")
                raise

    async def _close(connection: dict):
        async with lock:
            await async_client.shell_stop(connection["connection"])

    async def _progress():
        while num_left := len([x for x in tasks if not x.done()]):
            print(f"{num_left} hosts remaining...")
            await asyncio.sleep(5)

    tasks = [asyncio.create_task(_probe(x)) for x in connections]
    progress_task = asyncio.create_task(_progress())
    results = await asyncio.gather(*tasks, return_exceptions=True)
    await progress_task
    await asyncio.gather(*(asyncio.create_task(_close(x)) for x in connections), return_exceptions=True)
    # If we have no exceptions, we were successful
    return all(isinstance(x, dict) for x in results)


@cli.command()
@click.option("--category", "-c", default="*", help="Globbed category filter, defaults to *")
@click.option("--name", "-n", default="*", help="Globbed name filter, defaults to *")
@click.option("--type", "con_type", default="*", help="Globbed type filter, defaults to *")
@click.pass_obj
def probe(client: Client, category: str, name: str, con_type: str):
    """Probe connections, with optional filters"""
    connections = client.get_connections(categories=category, connections=name, types=con_type)
    # Restrict our connections to only shell connections, as we can't probe non-shell connections
    connections = [x for x in connections if x["usageCategory"] == "shell"]
    print(f"Spinning up probe requests for {len(connections)} hosts...")
    async_client = AsyncClient.from_sync_client(client)
    success = asyncio.run(probe_connections(async_client, connections))
    print("Probing finished with no errors!" if success else "Some errors during probing")


@cli.command()
@click.argument("remote", type=str)
@click.argument("local", type=click.File("wb"))
@click.pass_obj
def pull(client: Client, remote: str, local: click.File):
    """Read REMOTE (<connection_name>:/path/to/file) and write to LOCAL (/path/to/file)"""
    connection_name, remote_path = remote.rsplit(":", 1)
    connection = resolve_connection_name(client, connection_name)
    if not connection:
        print(f"Couldn't find connection UUID for {connection_name}")
        exit(1)
    client.shell_start(connection)
    print(f"Getting size of remote file {remote}...")
    try:
        stat_result = client.shell_exec(connection, f"stat -c %s {remote_path}")
        length = int(stat_result["stdout"])
    except Exception:
        length = 0
    print(f"Copying {remote} to {local.name}...")
    with tqdm(total=length, unit="B", unit_scale=True) as progress_bar:
        resp = client._fs_read(connection, remote_path)
        length = int(resp.headers.get("content-length", 0))
        progress_bar.total = length
        progress_bar.refresh()
        for chunk in resp.iter_content(1024):
            progress_bar.update(len(chunk))
            local.write(chunk)
    print("Done!")
    client.shell_stop(connection)


@cli.command()
@click.argument("local", type=click.File("rb"))
@click.argument("remote", type=str)
@click.pass_obj
def push(client: Client, local: click.File, remote: str):
    """Read LOCAL (/path/to/file) and write to REMOTE (<connection_name>:/path/to/file)"""
    connection_name, remote_path = remote.rsplit(":", 1)
    connection = resolve_connection_name(client, connection_name)
    if not connection:
        print(f"Couldn't find connection UUID for {connection_name}")
        exit(1)
    client.shell_start(connection)
    print(f"Uploading {local.name} to XPipe API...")
    blob_id = client.fs_blob(local)
    print(f"Copying uploaded file to {remote}...")
    client.fs_write(connection, blob_id, remote_path)
    client.shell_stop(connection)
    print("Done!")


@cli.command(name="exec")
@click.argument("command", type=str)
@click.argument("connection_name", type=str)
@click.option("-r", "--raw", is_flag=True, help="Print stdout directly instead of the whole result object")
@click.pass_obj
def fs_exec(client: Client, command: str, connection_name: str, raw: bool):
    """Execute COMMAND on CONNECTION_NAME"""
    connection = resolve_connection_name(client, connection_name)
    if not connection:
        print(f"Couldn't find connection UUID for {connection_name}")
        exit(1)
    client.shell_start(connection)
    result = client.shell_exec(connection, command)
    if raw:
        print(result["stdout"])
    else:
        print(json.dumps(result, indent=2))
    client.shell_stop(connection)


@cli.command()
@click.argument("script_file", type=click.File("rb"))
@click.argument("connection_name", type=str)
@click.option("-r", "--raw", is_flag=True, help="Print stdout directly instead of the whole result object")
@click.pass_obj
def run_script(client: Client, script_file: click.File, connection_name: str, raw: bool):
    """Run SCRIPT_FILE on CONNECTION_NAME"""
    connection = resolve_connection_name(client, connection_name)
    if not connection:
        print(f"Couldn't find connection UUID for {connection_name}")
        exit(1)
    client.shell_start(connection)
    blob_id = client.fs_blob(script_file)
    remote_path = client.fs_script(connection, blob_id)
    result = client.shell_exec(connection, remote_path)
    if raw:
        print(result["stdout"])
    else:
        print(json.dumps(result, indent=2))
    client.shell_stop(connection)


@cli.group()
def service():
    pass


@service.command()
@click.argument('host', type=str)
@click.argument('remote_port', type=int)
@click.argument('local_port', type=int, default=0)
@click.option('--autostart', is_flag=True, help="Make sure connection is enabled once added")
@click.option('--name', '-n', type=str, help="Set a custom name for the connection (defaults to HOST_REMOTEPORT)")
@click.pass_obj
def add(client: Client, host: str, remote_port: int, local_port: int, autostart: bool, name: Optional[str]):
    """Add a service on HOST from REMOTE_PORT to LOCAL_PORT (LOCAL_PORT defaults to REMOTE_PORT if omitted)"""
    if not local_port:
        local_port = remote_port
    host_uuid = resolve_connection_name(client, host, con_type='*ssh*')
    if not host_uuid:
        print(f"Couldn't find ssh-type connection UUID for {host}")
        exit(1)
    data = {"type": "customService", "remotePort": remote_port, "localPort": local_port, "host": {"storeId": host_uuid}}
    if not name:
        name = f"{host}_{remote_port}"
    service_uuid = client.connection_add(name=name, conn_data=data)
    if autostart:
        client.connection_toggle(service_uuid, state=True)


@service.command()
@click.argument('service_name', type=str)
@click.pass_obj
def remove(client: Client, service_name: str):
    """Remove service SERVICE_NAME"""
    service_uuid = resolve_connection_name(client, service_name, con_type='*service*')
    if not service_uuid:
        print(f"Couldn't find service UUID for {service_name}")
        exit(1)
    client.connection_remove(service_uuid)


@service.command()
@click.argument('service_name', type=str)
@click.option('--stop-others', is_flag=True, help="Stop other services before starting this one")
@click.pass_obj
def start(client: Client, service_name: str, stop_others: bool):
    """Start an existing service by the name of SERVICE_NAME"""
    service_uuid = resolve_connection_name(client, service_name, con_type='*service*')
    if not service_uuid:
        print(f"Couldn't find connection UUID for {service_name}")
        exit(1)
    if stop_others:
        print("Stopping all enabled services...")
        all_services = client.get_connections(types="*service*")
        active_services = [x for x in all_services if x["cache"].get("sessionEnabled", False)]
        for active_service in active_services:
            print(f"Stopping {active_service['name'][-1]}...")
            client.connection_toggle(active_service["connection"], state=False)
    print(f"Activating service {service_name}...")
    client.connection_toggle(service_uuid, state=True)
    print("Activated.")


@service.command()
@click.argument('service_name', type=str)
@click.pass_obj
def stop(client: Client, service_name: str):
    """Stop an existing service by the name of SERVICE_NAME"""
    service_uuid = resolve_connection_name(client, service_name, con_type='*service*')
    if not service_uuid:
        print(f"Couldn't find connection UUID for {service_name}")
        exit(1)
    print(f"Deactivating service {service_name}...")
    client.connection_toggle(service_uuid, state=False)
    print("Deactivated.")


def handled_cli():
    try:
        return cli()
    except HTTPError as e:
        print(e)


if __name__ == "__main__":
    handled_cli()
