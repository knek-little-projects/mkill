#!/usr/bin/env python3
import json
import os
import sys
import time

if len(sys.argv) == 1:
    config_path = "/etc/mkill.json"
elif len(sys.argv) == 2:
    config_path = sys.argv[1]
else:
    print("Usage: mkill [config_path]")
    exit(1)

with open(config_path) as config_file:
    config = json.load(config_file)

threshold = config["threshold"]
cmd = config["cmd"]

args = config.get("args") or [[]]
test_sleep = config.get("testSleep", 1)
cmd_sleep = config.get("cmdSleep", 0)


def memcount():
    """
    Returns available memory (RAM) in kB
    """
    with open("/proc/meminfo") as meminfo:
        for line in meminfo:
            if "MemAvail" in line:
                return int(''.join(c for c in line if c.isdigit()))


while True:
    time.sleep(test_sleep)
    avail = memcount()
    if avail < threshold:
        print("memcount %d < threshold %d" % (avail, threshold))
        for a in args:
            os.system(cmd % tuple(a))
            time.sleep(cmd_sleep)
    else:
        print("memcount %d >= threshold %d" % (avail, threshold))
