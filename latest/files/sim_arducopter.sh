#!/usr/bin/env bash

set -e

cd /ardupilot/ArduCopter
sim_vehicle.py -N -m --logfile=$(mavproxy_logpath arducopter)
