Kill unnecessary processes if remaining RAM is getting too low
==============================================================

Config
------

Open mkill.json:
* threshold - memory threshold in kB
* cmd - command pattern to run if available memory is lower then the threshold
* args - arguments to command pattern
* testSleep - sleep this number of seconds before each memory test
* cmdSleep - sleep this number of seconds before running each cmd

Example:
* Kill `nano` if available RAM &lt; 100kB
```
{"threshold": 100, "cmd": "pkill %s", "args": [["nano"]]}
```
* Kill all user processes if available RAM &lt; 100000kB
```
{"threshold": 100000, "cmd": "pkill -u user"}
```

Installation
------------
```
cp mkill.json /etc/
cp mkill-daemon.py /usr/bin/mkill-daemon
cp mkill.service /etc/systemd/system/
chown root:root /etc/mkill.json /usr/bin/mkill-daemon /etc/systemd/system/mkill.service
systemctl daemon-reload
service mkill restart
```

Requirements
------------
```
python3
systemd
/proc/meminfo
pkill
```