#!/usr/bin/env bash

set -e

cd /ardupilot/ArduPlane
sim_vehicle.py -N -m --logfile=$(mavproxy_logpath arduplane)
