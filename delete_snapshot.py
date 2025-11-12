#!/usr/bin/env python3
"""Delete a snapshot."""

import sys

import list_snapshots
from api import dolib


def main() -> None:
    print(f"Snapshot to delete : {snapshot_id}")
    d.delete_snapshot(snapshot_id=snapshot_id)
    print("Snapshot deletion completed.")


if __name__ == "__main__":
    d = dolib.Do()
    d.get_client()
    snapshot_id = sys.argv[1] if len(sys.argv) > 1 else None
    if not snapshot_id:
        print("Usage: delete_snapshot.py <snapshot_id>")
        list_snapshots.main()
        sys.exit(1)
    main()
