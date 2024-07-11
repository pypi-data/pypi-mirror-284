import argparse
import asyncio
from pathlib import Path
from resemble.admin import exim_client
from resemble.aio.workflows import Workflow
from resemble.cli import terminal
from resemble.cli.rc import ArgumentParser
from resemble.v1alpha1.admin import exim_pb2_grpc


def register_export_and_import(parser: ArgumentParser):

    def add_common_args(subcommand):
        # TODO: Should this prepend an application id, similar to
        # `cloud._application_gateway`, or expect it to be fully
        # formed?
        subcommand.add_argument(
            '--gateway-address',
            type=str,
            help="the gateway address of the Resemble application",
            required=True,
        )
        subcommand.add_argument(
            '--gateway-secure-channel',
            type=bool,
            help="whether to use a secure channel to connect to the gateway",
            default=True,
        )

    add_common_args(parser.subcommand('export'))
    parser.subcommand('export').add_argument(
        '--directory',
        type=str,
        help="a directory to export data to, as JSON-lines files",
        required=True,
    )

    add_common_args(parser.subcommand('import'))
    parser.subcommand('import').add_argument(
        '--directory',
        type=str,
        help="a directory to import data from, as JSON-lines files",
        required=True,
    )


def _exim_stub(args: argparse.Namespace) -> exim_pb2_grpc.EximStub:
    workflow = Workflow(
        name="resemble-cli",
        # TODO: See #2274.
        #bearer_token=...,
        gateway=args.gateway_address,
        secure_channel=args.gateway_secure_channel,
    )
    return exim_pb2_grpc.EximStub(workflow.legacy_grpc_channel())


async def exim_export(args: argparse.Namespace) -> int:
    """Implementation of the 'export' subcommand."""

    dest_dir = Path(args.directory)
    if dest_dir.is_dir() and any(dest_dir.iterdir()):
        terminal.fail(f"Destination directory `{dest_dir}` must be empty.\n\n")

    exim = _exim_stub(args)
    try:
        await exim_client.exim_export(exim, dest_dir)
    except Exception as e:
        terminal.fail(
            f"Failed to export: {e}\n\nPlease report this issue to the maintainers."
        )

    terminal.info(f"Exported to: `{dest_dir}`")
    return 0


async def exim_import(args: argparse.Namespace) -> int:
    """Implementation of the 'import' subcommand."""

    src_dir = Path(args.directory)
    if not src_dir.is_dir() or not any(src_dir.iterdir()):
        terminal.fail(f"Source directory `{src_dir}` must be non-empty.\n\n")

    exim = _exim_stub(args)
    try:
        await asyncio.gather(
            *(
                exim_client.exim_import(exim, path)
                for path in src_dir.iterdir()
            )
        )
    except Exception as e:
        terminal.fail(
            f"Failed to import: {e}\n\nPlease report this issue to the maintainers."
        )

    terminal.info(f"Imported from: `{src_dir}`")
    return 0
