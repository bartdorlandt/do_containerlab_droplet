#!/usr/bin/env python3
"""Shutdown a droplet and create a snapshot from it."""

import time
from datetime import datetime

from rich import print as rprint

from api import dolib


def amount_of_droplets(droplets: dict) -> int:
    """Return the amount of droplets."""
    return droplets["meta"]["total"]


def main():
    d = dolib.Do()
    d.get_client()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    droplets = d.get_droplets()

    if amount_of_droplets(droplets) != 1:
        # TODO
        print("TODO: print and action on multiple droplets")
        return

    rprint("Droplet info:\n", droplets["droplets"][0])
    droplet_id = droplets["droplets"][0]["id"]

    d.droplet_shutdown(droplet_id=droplet_id)
    status = None
    while status != "off":
        print("Waiting for the droplet to be shutdown...")
        time.sleep(3)
        droplet_status = d.get_droplet_by_id(droplet_id=droplet_id)
        status = droplet_status["droplet"]["status"]

    print("Droplet shutdown completed. Continue with snapshot creation.")

    snap_details = d.create_snapshot_from_droplet(
        droplet_id=droplet_id,
        name=f"from_running-{date_now}",
    )
    action_id = snap_details["action"]["id"]
    status = None
    while status != "completed":
        print("Waiting for the snapshot to be created...")
        time.sleep(10)
        snap_status = d.get_droplet_by_action(droplet_id=droplet_id, action_id=action_id)
        status = snap_status["action"]["status"]
        print("Snapshot status:", status)

    print("Snapshot details:\n", snap_status)
    print("Droplet shutdown and snapshot creation completed.")

    print("Delete the droplet now? [y/N]")
    delete_droplet = input().strip().lower()
    if delete_droplet == "y":
        d.delete_droplet(droplet_id=droplet_id)
        print("Droplet deleted.")
    else:
        print("Droplet not deleted. You can delete it later manually.")


if __name__ == "__main__":
    main()
