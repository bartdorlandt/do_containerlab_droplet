#!/usr/bin/env python3
"""List all snapshots."""

from rich import print as rprint

from api import dolib


def main():
    d = dolib.Do()
    d.get_client()
    snapshots = d.get_snapshots()
    rprint("snapshots:", snapshots)


if __name__ == "__main__":
    main()
