#!/usr/bin/env python3
"""List all droplets."""

from rich import print as rprint

from api import dolib


def main():
    d = dolib.Do()
    d.get_client()
    # date fformat = "%Y-%m-%d %H:%M:%S"
    droplets = d.get_droplets()
    rprint("droplets:", droplets)


if __name__ == "__main__":
    main()
