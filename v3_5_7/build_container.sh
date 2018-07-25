#!/usr/bin/env bash

set -e

docker build -t asciich/ardupilot_sitl:3.5.7 . ${1}

