#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]
then
  echo "Usage:"
  echo "  mkill <memory threshold (kB)> <process names...>"
  exit 1
fi

while sleep 1
do
  memcount=$(cat /proc/meminfo | grep MemAvail | grep -oE '[0-9]+')
  if [ $memcount -lt $1 ]
  then
    echo "memcount $memcount < threshold $1"
    echo KILLING
    for p in ${*:2}
    do
      pkill -KILL $p
      pkill -KILL $p
      pkill -KILL $p
      pkill -KILL $p
    done
  else
    echo "memcount $memcount >= threshold $1"
  fi
done
