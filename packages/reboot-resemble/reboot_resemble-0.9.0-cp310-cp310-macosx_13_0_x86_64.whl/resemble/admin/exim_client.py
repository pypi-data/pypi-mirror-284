import aiofiles
import asyncio
import grpc
import json
from pathlib import Path
from resemble.aio.types import ConsensusId
from resemble.v1alpha1.admin import exim_pb2, exim_pb2_grpc
from resemble.v1alpha1.admin.exim_pb2 import (
    ExportRequest,
    ImportRequest,
    ListConsensusesRequest,
)
from typing import AsyncIterator


async def _export(
    exim: exim_pb2_grpc.EximStub,
    consensus_id: ConsensusId,
    dest_path: Path,
) -> None:
    while True:
        try:
            async with aiofiles.open(dest_path, 'wb') as output:
                async for response in exim.Export(
                    ExportRequest(consensus_id=consensus_id),
                ):
                    await output.write(
                        b'{"state_type": %b, "actor_id": %b, "state": %b}\n' %
                        (
                            json.dumps(response.actor_id.state_type).encode(),
                            json.dumps(response.actor_id.actor_id).encode(),
                            response.state_json,
                        )
                    )
            return
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                # We were sent to the incorrect consensus: try again until
                # we get the right one.
                continue
            raise


async def exim_export(
    exim: exim_pb2_grpc.EximStub, dest_directory: Path
) -> None:
    """Export one JSON-lines file per consensus to the given directory."""
    dest_directory.mkdir(parents=True, exist_ok=True)

    response = await exim.ListConsensuses(ListConsensusesRequest())
    # TODO: Throttle the total number of outstanding requests.
    await asyncio.gather(
        *(
            _export(
                exim,
                consensus_id,
                dest_directory / f"{consensus_id}.json",
            ) for consensus_id in response.consensus_ids
        )
    )


async def _import(exim: exim_pb2_grpc.EximStub, src_path: Path) -> None:

    async def import_stream() -> AsyncIterator[ImportRequest]:
        async with aiofiles.open(src_path, 'r') as infile:
            async for line in infile:
                entry = json.loads(line)
                yield ImportRequest(
                    actor_id=exim_pb2.ActorId(
                        state_type=entry["state_type"],
                        actor_id=entry["actor_id"],
                    ),
                    # TODO: Could add a custom JSON loads hook to avoid
                    # round-tripping the actor's state here.
                    state_json=json.dumps(entry["state"]).encode(),
                )

    await exim.Import(import_stream())


async def exim_import(
    exim: exim_pb2_grpc.EximStub, src_directory: Path
) -> None:
    """Import all JSON-lines files in the given directory to the server."""
    # TODO: Throttle the number of requests and/or make a best effort to
    # direct items at the "correct" nodes using a placement client.
    await asyncio.gather(
        *(_import(exim, path) for path in src_directory.iterdir())
    )
