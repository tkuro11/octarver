#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "Usage $1 <NOTE NAME> (#count)"
    exit 1
fi

base=$(./octaver.py $1)

if [ $2 ]; then to=$2
else
    to=8
fi

for i in `seq 1 $to`; do
    echo -n "x$i "
    ./octaver.py `echo $i*$base|bc`
done
