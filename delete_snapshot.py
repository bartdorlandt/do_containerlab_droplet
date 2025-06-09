#!/usr/bin/env python3
"""Delete a snapshot."""

import sys

from rich import print as rprint

from api import dolib


def main() -> None:
    snapshot = d.delete_snapshot(snapshot_id=snapshot_id)

    rprint("Snapshot deleted:", snapshot)
    print("Snapshot deletion completed.")


if __name__ == "__main__":
    d = dolib.Do()
    d.get_client()
    snapshot_id = sys.argv[1] if len(sys.argv) > 1 else None
    if not snapshot_id:
        print("Usage: delete_snapshot.py <snapshot_id>")
        rprint(d.get_snapshots())
        sys.exit(1)
    main()
