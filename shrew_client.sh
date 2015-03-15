#!/bin/sh
rto=1
#a1=net.get('a1')
#serverIP=a1.IP()
while true; do
	iperf -c 10.0.0.1 -u -b 10M -t 1 &
	rto=$($rto*2)
	echo 'rto:'
	echo $rto 
	sleep $rto 
done
