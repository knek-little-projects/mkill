#!/bin/bash

if [ $(whoami) != root ]
then
  echo "Expected user root"
  exit 1
fi

cp -i mkill.json /etc/
cp -i mkill-daemon.py /usr/bin/mkill-daemon
cp -i mkill.service /etc/systemd/system/
chown root:root /etc/mkill.json /usr/bin/mkill-daemon /etc/systemd/system/mkill.service
systemctl daemon-reload
service mkill restart
