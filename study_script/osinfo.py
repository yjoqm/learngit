#!/usr/bin/env python
# coding=utf-8
import platform

profile = {
    "mac_ver：" : platform.mac_ver(),
    "machine:": platform.machine(),
    "node:": platform.node(),
    "platform:": platform.platform(),
    "system:": platform.system(),
    "uname:": platform.uname(),
    "version:":platform.version(),
    "release:": platform.release(),
    "Linux Distribution:": platform.linux_distribution(),
    "Architecture:": platform.architecture(),
}

for key in profile:
     print key + str(profile[key])

