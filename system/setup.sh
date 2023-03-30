#!/bin/sh
#
# Copyright 2022 Stéphane Caron
#
# Meant to be run from the host, not from the target (Raspberry Pi).

set -e

if [ $# -ne 1 ]
then
    echo "Usage: $0 <[user@]host>"
    exit
fi

SCRIPT_DIR=$(dirname $0)
UPKIE=${1}  # [user@]hostname of target platform

scp ${SCRIPT_DIR}/remote/setup-system.py ${UPKIE}:setup-system.py
ssh ${UPKIE} sudo ./setup-system.py
