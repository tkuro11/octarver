#!/usr/bin/env zsh

base=$(./octaver.py $1)

if [ $2 ]; then to=$2 else to=8 fi

for i in `seq 1 $to`; do
    echo -n "x$i "
    ./octaver.py $((i*base))
done
