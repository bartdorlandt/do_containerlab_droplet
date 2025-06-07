#!/bin/bash

# Reinstall unattended-upgrades service and enable it
apt-get -y install unattended-upgrades
systemctl daemon-reload
systemctl enable unattended-upgrades.service

# Clean up apt cache and remove unnecessary packages
apt-get -y autoclean && apt-get -y autoremove --purge
