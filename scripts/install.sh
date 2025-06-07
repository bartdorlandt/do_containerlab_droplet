#!/bin/bash
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
export DEBIAN_FRONTEND=noninteractive

# Update your system:
apt-get update && apt-get dist-upgrade -y
apt-get install -y curl git

# task
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin
task --completion bash > /etc/bash_completion.d/task
