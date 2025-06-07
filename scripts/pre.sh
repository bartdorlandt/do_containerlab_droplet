#!/bin/bash

# Stop this service to not interfere with the installation:
systemctl stop unattended-upgrades.service
systemctl kill unattended-upgrades.service

# Also removing the service, since it was still interfering with the installation
apt-get -y remove unattended-upgrades
systemctl daemon-reload
