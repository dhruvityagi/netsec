#!/bin/sh
#Version 1
rto=1
while true; do
	iperf -c 10.0.0.1 -u -b 5M -t 0.5 &
	rto=$($rto*2)
	echo 'rto:'
	echo $rto 
	sleep $rto 
done
