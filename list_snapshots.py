#!/usr/bin/env python3
"""List all snapshots."""

from api import dolib


def main():
    d = dolib.Do()
    d.get_client()
    snapshots = d.get_snapshots()
    for d in snapshots.get("snapshots", []):
        print(
            f"name: {d['name']} \t"
            f"id: {d['id']} \t"
            f"regions: {d['regions']} \t"
            f"resource_type: {d['resource_type']} \t"
            f"size_gigabytes: {d['size_gigabytes']}"
        )


if __name__ == "__main__":
    main()
