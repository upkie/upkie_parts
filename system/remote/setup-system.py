#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#     setup-system.py from github.com:mjbots/quad
#     Copyright 2018-2020 Josh Pieper
#     License: Apache-2.0


"""
Set up a Raspberry Pi 4b to run software for Upkie.

The base operating system should already be installed. This script is intended
to be run as root, like: ``sudo ./setup-system.py``.
"""

import os
import pathlib
import shutil
import subprocess
import time

ORIG_SUFFIX = time.strftime(".orig-%Y%m%d-%H%M%S")

# Utility functions
# =================


def run(*args, **kwargs):
    print("run: " + args[0])
    subprocess.check_call(*args, shell=True, **kwargs)


def ensure_present(filename, line):
    """
    Ensure a given line is present in a named file, and add it if not.

    Args:
        filename: Path to file.
        line: Line that should be present in the file's content.
    """
    current_content = [
        x.strip() for x in open(filename, encoding="utf-8").readlines()
    ]
    if line.strip() in current_content:
        # Yes, the line is already present there
        return

    shutil.copy(filename, filename + ORIG_SUFFIX)

    print("ensure_present({}): Adding: {}".format(filename, line))

    # Nope, we need to add it.
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def ensure_contents(filename, contents):
    """
    Ensure the given file has exactly the given contents.

    Args:
        filename: Path to file.
        contents: File contents.
    """
    pathlib.Path(filename).parent.mkdir(parents=True, exist_ok=True)

    if os.path.exists(filename):
        existing = open(filename, encoding="utf-8").read()
        if existing == contents:
            return
        shutil.copy(filename, filename + ORIG_SUFFIX)

    print("ensure_contents({}): Updating".format(filename))

    with open(filename, "w", encoding="utf-8") as f:
        f.write(contents)


def set_config_var(name, value):
    """
    Set the given variable in /boot/config.txt.

    Args:
        name: Variable name.
        value: Value to set.
    """
    contents = open("/boot/config.txt", encoding="utf-8").readlines()

    new_value = "{}={}".format(name, value)

    maybe_value = [x for x in contents if x.startswith("{}=".format(name))]
    if len(maybe_value) == 1 and maybe_value[0].strip() == new_value:
        return

    new_contents = [
        x for x in contents if not x.startswith("{}=".format(name))
    ] + [new_value + "\n"]

    shutil.copy("/boot/config.txt", "/boot/config.txt" + ORIG_SUFFIX)

    print("set_config_var({})={}".format(name, value))

    open("/boot/config.txt", "w", encoding="utf-8").write(
        "".join([x for x in new_contents])
    )


# Instructions
# ============


def install_packages():
    run("apt-get install --yes hostapd dnsmasq")


def configure_camera():
    # run("raspi-config nonint do_camera 0")
    print("configure_camera(): Not implemented yet")


def configure_ssh():
    # run("raspi-config nonint do_ssh 0")
    print("configure_ssh(): Not implemented yet")


def configure_keyboard():
    ensure_contents(
        "/etc/default/keyboard",
        """# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT=""
XKBOPTIONS=""

BACKSPACE="guess"
""",
    )


def configure_cpu_isolation(filename="/boot/cmdline.txt"):
    """
    Make sure CPU isolation is configured.

    Args:
        filename: Path to the boot cmdline configuration file.
    """
    keyword, value = "isolcpus", "1,2,3"
    file_content = [
        x.strip() for x in open(filename, encoding="utf-8").readlines()
    ]
    assert len(file_content) == 1

    new_item = "{}={}".format(keyword, value)
    items = [x.strip() for x in file_content[0].split(" ")]
    present = [x for x in items if x == keyword or x.startswith(keyword + "=")]
    if len(present) > 0:
        new_items = [
            x
            if not (x == keyword or x.startswith(keyword + "="))
            else new_item
            for x in items
        ]
    else:  # len(present) == 0
        new_items = items + [new_item]

    if new_items == items:
        print("configure_cpu_isolation(): Already configured")
        return

    print(
        "configure_cpu_isolation(): Adding {}={} to {}".format(
            keyword, value, filename
        )
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(" ".join(new_items) + "\n")


def disable_ntp():
    """
    Disable NTP synchronization.
    """
    run("timedatectl set-ntp false")


def configure_access_point(
    ssid="Upkie",
    wlan_prefix="192.168.0",
    wpa_passphrase="LivingRoomRoaming",
    country_code="FR",
    eth_prefix="192.168.1",
):
    """
    Configure the Pi as an access point.

    Args:
        ssid: SSID of the Wi-Fi network.

    Note:
        The robot's IP suffix on both eth0 and wlan0 interfaces is 42. IP
        address suffixes on the wireless network are assigned from 100 to 110.
    """

    def configure_interfaces(wlan_prefix, eth_prefix):
        ensure_contents(
            "/etc/network/interfaces",
            """# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
""",
        )
        ensure_contents(
            "/etc/dhcpcd.conf",
            f"""# Configuration for dhcpcd.
# See dhcpcd.conf(5) for details.

# Allow users of this group to interact with dhcpcd via the control socket.
#controlgroup wheel

# Inform the DHCP server of our hostname for DDNS.
hostname

# Use the hardware address of the interface for the Client ID.
clientid
# or
# Use the same DUID + IAID as set in DHCPv6 for DHCPv4 ClientID as per RFC4361.
# Some non-RFC compliant DHCP servers do not reply with this set.
# In this case, comment out duid and enable clientid above.
#duid

# Persist interface configuration when dhcpcd exits.
persistent

# Rapid commit support.
# Safe to enable by default because it requires the equivalent option set
# on the server to actually work.
option rapid_commit

# A list of options to request from the DHCP server.
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
# Respect the network MTU. This is applied to DHCP routes.
option interface_mtu

# Most distributions have NTP support.
#option ntp_servers

# A ServerID is required by RFC2131.
require dhcp_server_identifier

# Generate SLAAC address using the Hardware Address of the interface
#slaac hwaddr
# OR generate Stable Private IPv6 Addresses based from the DUID
slaac private

# Static IP configuration for debugging
interface eth0
static ip_address={eth_prefix}.42/24
static routers={eth_prefix}.1

# Wireless access point configuration for Upkie
interface wlan0
nohook wpa_supplicant
static ip_address={wlan_prefix}.42/24
static routers={wlan_prefix}.1
""",
        )

    def configure_hostapd(ssid, wpa_passphrase, country_code):
        ensure_contents(
            "/etc/hostapd/hostapd.conf",
            f"""country_code={country_code}

interface=wlan0
driver=nl80211
ssid={ssid}
hw_mode=a
channel=36
ieee80211n=1
require_ht=1
ieee80211ac=1
require_vht=1
ieee80211d=1
ieee80211h=0

ht_capab=[HT40+][SHORT-GI-20][DSSS_CK-40][MAX-AMSDU-3839]
vht_capab=[MAX-MDPU-3895][SHORT-GI-80][SU-BEAMFORMEE]

vht_oper_chwidth=1
vht_oper_centr_freq_seg0_idx=42

wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0

wpa=2
wpa_passphrase={wpa_passphrase}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
""",
        )
        ensure_present(
            "/etc/default/hostapd", 'DAEMON_CONF="/etc/hostapd/hostapd.conf"'
        )
        run("systemctl unmask hostapd")
        run("systemctl enable hostapd")
        run("systemctl start hostapd")
        run("systemctl daemon-reload")

    def configure_dnsmasq(wlan_prefix):
        ensure_contents(
            "/etc/dnsmasq.conf",
            f"""interface=wlan0
listen-address=::1,127.0.0.1,{wlan_prefix}.42
domain-needed
bogus-priv
dhcp-range={wlan_prefix}.100,{wlan_prefix}.110,255.255.255.0,24h
""",
        )

    run("rfkill unblock all")
    configure_interfaces(wlan_prefix, eth_prefix)
    configure_hostapd(ssid, wpa_passphrase, country_code)
    configure_dnsmasq(wlan_prefix)


if __name__ == "__main__":
    if os.getuid() != 0:
        raise RuntimeError("must be run as root")

    install_packages()
    configure_camera()
    configure_ssh()
    configure_keyboard()
    configure_cpu_isolation()
    disable_ntp()
    configure_access_point()