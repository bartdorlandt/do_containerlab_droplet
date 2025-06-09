#!/usr/bin/env python3
"""Delete a droplet."""

import sys

from rich import print as rprint

from api import dolib


def main() -> None:
    droplet = d.delete_droplet(droplet_id=droplet_id)

    rprint("Droplet deleted:", droplet)
    print("Droplet deletion completed.")


if __name__ == "__main__":
    d = dolib.Do()
    d.get_client()
    droplet_id = sys.argv[1] if len(sys.argv) > 1 else None
    if not droplet_id:
        print("Usage: delete_droplet.py <droplet_id>")
        rprint(d.get_droplets())
        sys.exit(1)
    main()
