#!/bin/sh
#
# Copyright 2022 Stéphane Caron
#
# Run this script from the host to configure a target Raspberry Pi system.

set -e

if [ $# -ne 1 ]
then
    echo "Usage: $0 <[user@]host>"
    exit
fi

CURDIR=$(dirname $0)
UPKIE=${1}  # [user@]hostname of target platform

scp ${CURDIR}/scripts ${UPKIE}:scripts
ssh ${UPKIE} sudo ./scripts/setup-system.py
