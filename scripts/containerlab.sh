#!/bin/bash

# https://containerlab.dev/install/
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"

# Nokia image
docker pull ghcr.io/srl-labs/clab

# Other docker images (juniper, arista, etc.) with a tar.gz extension
for file in /root/docker_images/*.tar.gz; do
    if [[ -f "$file" ]]; then
        docker load -i "$file"
        echo "Loaded $file into Docker."
        rm -f "$file"
    else
        echo "No .tar.gz files found in /root/docker_images."
    fi
done

echo "Containerlab installed successfully."
