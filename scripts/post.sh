#!/bin/bash

wait_for_lock() {
  while lsof $1 ; do sleep 15; done;
}

wait_for_lock "/var/lib/dpkg/lock-frontend"
# Clean up apt cache and remove unnecessary packages
apt-get -y autoclean && apt-get -y autoremove --purge
