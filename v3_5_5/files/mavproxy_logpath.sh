#!/usr/bin/env bash

set -e

SIM_NAME="arducpilot"

if [ "${1}" != "" ] ; then
    SIM_NAME="${1}"
fi

LOG_NAME=$(date "+%Y%m%d_%H%M%S_${SIM_NAME}_sitl.log")
LOG_PATH="/var/log/mavproxy/${LOG_NAME}"
echo ${LOG_PATH}
