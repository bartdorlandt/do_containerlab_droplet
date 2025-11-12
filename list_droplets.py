#!/usr/bin/env python3
"""List all droplets."""

from api import dolib


def main():
    d = dolib.Do()
    d.get_client()
    droplets = d.get_droplets()
    for d in droplets.get("droplets", []):
        print(
            f"name: {d['name']} \t"
            f"id: {d['id']} \t"
            f"status: {d['status']} \t"
            f"vCPUs: {d['vcpus']} \t"
            f"memory: {d['memory']}"
        )


if __name__ == "__main__":
    main()
