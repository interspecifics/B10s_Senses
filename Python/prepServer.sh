#!/bin/bash

# makes sure jack and scsynth are running
uname=`whoami`

isjack=`ps -u $uname | grep jack | grep -v grep | wc -l`
if [ $isjack -lt 1 ]
then
    jackd -p32 -dalsa -dhw:0,0 -p1024 -n3 -s &
fi

issynth=`ps -u $uname | grep scsynth | grep -v grep | wc -l`
if [ $issynth -ge 1 ]
then
    killsynthid=`ps -u $uname | awk '/scsynth/{print $1}'`
    kill -9 $killsynthid
fi
scsynth -u 57110 &
