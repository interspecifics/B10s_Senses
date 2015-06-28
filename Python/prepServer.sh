#!/bin/bash

# makes sure jack and scsynth are running
uname=`whoami`

# kills all python and sudo processes
kpids=`ps -u root | grep 'ython\|sudo' | grep -v grep | awk '/ython|sudo/{print $1}'`
sudo kill -9 $kpids

isjack=`ps -u $uname | grep jack | grep -v grep | wc -l`
if [ $isjack -ge 1 ]
then
    killjackid=`ps -u $uname | awk '/jack/{print $1}'`
    kill -9 $killjackid
fi
jackd -p32 -dalsa -dhw:0,0 -p1024 -n3 -s &

issynth=`ps -u $uname | grep scsynth | grep -v grep | wc -l`
if [ $issynth -ge 1 ]
then
    killsynthid=`ps -u $uname | awk '/scsynth/{print $1}'`
    kill -9 $killsynthid
fi
scsynth -u 57110 &
