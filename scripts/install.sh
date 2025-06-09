#!/bin/bash

wait_for_lock() {
  while lsof $1 ; do sleep 15; done;
}

echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
export DEBIAN_FRONTEND=noninteractive

# Upgrade all packages and remove anything that's not needed
wait_for_lock "/var/lib/apt/lists/lock"
apt-get update

wait_for_lock "/var/lib/dpkg/lock-frontend"
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -yq

wait_for_lock "/var/lib/dpkg/lock-frontend"
apt-get install -y curl git


# task
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin
task --completion bash > /etc/bash_completion.d/task
