#!/usr/bin/env python3
"""List full droplet details for a given id."""

import sys

from rich import print as rprint

from api import dolib


def main():
    droplet_id = int(sys.argv[1])
    d = dolib.Do()
    d.get_client()
    droplet = d.get_droplet_by_id(droplet_id=droplet_id)
    rprint(droplet)


if __name__ == "__main__":
    main()
