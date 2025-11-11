#!/usr/bin/env python3
"""Create a droplet from a snapshot."""

import time

from environs import env
from rich import print as rprint

from api import dolib


def amount_of_snapshots(snapshots: dict) -> int:
    """Return the amount of snapshots."""
    return snapshots["meta"]["total"]


def main() -> None:
    d = dolib.Do()
    d.get_client()
    snapshots = d.get_snapshots()

    if amount_of_snapshots(snapshots) == 1:
        snap_id = snapshots["snapshots"][0]["id"]
    else:
        rprint("snapshots:", snapshots)
        snap_id = input("Which ID of the snapshots do you want to create a droplet for?  ")
        # verify
        for snap in snapshots["snapshots"]:
            if snap["id"] == snap_id:
                # snapshot found
                break
        else:
            print(f"Snapshot ID {snap_id} not found in the list. Feel free to retry")
            return
    print("Creating droplet from snapshot ID:", snap_id)

    droplet = d.create_droplet(
        name=f"clab.{snap_id}",
        region=env("region"),
        size=env("size"),
        image=snap_id,
    )
    droplet_id = droplet["droplet"]["id"]

    status = None
    while status != "active":
        print("Waiting for the droplet to be created...")
        # wait for the droplet to be shutdown
        time.sleep(5)
        # get the status of the droplet
        droplet_status = d.get_droplet_by_id(droplet_id=droplet_id)
        status = droplet_status["droplet"]["status"]

    ip = droplet_status["droplet"]["networks"]["v4"][0]["ip_address"]

    rprint("Droplet created successfully.", droplet_status)
    print("Droplet creation completed.")
    print(f"Droplet ID: {droplet_id} IP address: {ip}")


if __name__ == "__main__":
    env.read_env()
    main()
