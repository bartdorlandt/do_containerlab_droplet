"""DigitalOcean API client wrapper for managing droplets and snapshots."""

import os

from pydo import Client


class Do:
    """DigitalOcean API client wrapper."""

    client: Client
    snapshots: dict
    droplets: dict
    ssh_keys: list[int]

    def __init__(self) -> None:
        """Initialize the DigitalOcean API client."""
        self._api = os.getenv("DIGITALOCEAN_ACCESS_TOKEN")
        if not self._api or self._api == "":
            raise ValueError("DIGITALOCEAN_ACCESS_TOKEN environment variables must be set.")

    def get_client(self) -> Client:
        """Get the DigitalOcean API client."""
        self.client = Client(token=self._api)
        self.get_ssh_keys()
        return self.client

    # snapshots
    def get_snapshots(self) -> dict:
        """Get all snapshots."""
        self.snapshots = self.client.snapshots.list()
        return self.snapshots

    def delete_snapshot(self, snapshot_id: str) -> None:
        """Delete a snapshot by its ID."""
        self.client.snapshots.delete(snapshot_id=snapshot_id)

    # droplets
    def get_droplets(self) -> dict:
        """Get all droplets."""
        self.droplets = self.client.droplets.list()
        return self.droplets

    def get_droplet_by_id(self, droplet_id: int) -> dict:
        """Get droplet by id."""
        return self.client.droplets.get(droplet_id=droplet_id)

    def get_droplet_by_tag(self, tag: str) -> dict:
        """Get droplets by tag."""
        return self.client.droplets.list(tag_name=tag)

    def get_droplet_by_action(self, droplet_id: int, action_id: int) -> dict:
        """Get droplet by action ID."""
        return self.client.droplet_actions.get(droplet_id=droplet_id, action_id=action_id)

    def droplet_shutdown(self, droplet_id: str) -> None:
        """Shutdown a droplet by its ID."""
        req = {"type": "shutdown"}
        return self.client.droplet_actions.post(droplet_id=droplet_id, body=req)

    def delete_droplet(self, droplet_id: int) -> None:
        """Delete a droplet by its ID."""
        return self.client.droplets.destroy(droplet_id=droplet_id)

    def create_snapshot_from_droplet(self, droplet_id: str, name: str) -> None:
        """Create a snapshot of a droplet by its ID."""
        req = {"type": "snapshot", "name": name}
        return self.client.droplet_actions.post(droplet_id=droplet_id, body=req)

    def create_droplet(self, name: str, region: str, size: str, image: str) -> dict:
        """Create a new droplet."""
        req = {
            "name": name,
            "region": region,
            "size": size,
            "image": image,
            "monitoring": True,
            "tags": ["api-created", "clab"],
            "ssh_keys": self.ssh_keys,
        }

        return self.client.droplets.create(body=req)

    def get_ssh_keys(self) -> dict:
        """Get SSH keys."""
        keys = self.client.ssh_keys.list()
        self.ssh_keys = [key.get("id") for key in keys["ssh_keys"]]
        return self.client.ssh_keys.list()
