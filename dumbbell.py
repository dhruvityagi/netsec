# CMU 18731 HW2
# Code referenced from:git@bitbucket.org:huangty/cs144_bufferbloat.git
# Edited by: Deepti Sunder Prakash

#!/usr/bin/python

from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

from subprocess import Popen, PIPE
from time import sleep, time
from multiprocessing import Process
from argparse import ArgumentParser

import sys
import os

# Parse arguments

parser = ArgumentParser(description="Shrew tests")
parser.add_argument('--bw-host', '-B',
                    dest="bw_host",
                    type=float,
                    action="store",
                    help="Bandwidth of host links",
                    required=True)
parser.add_argument('--bw-net', '-b',
                    dest="bw_net",
                    type=float,
                    action="store",
                    help="Bandwidth of network link",
                    required=True)
parser.add_argument('--delay',
                    dest="delay",
                    type=float,
                    help="Delay in milliseconds of host links",
                    default='10ms')
parser.add_argument('-n',
                    dest="n",
                    type=int,
                    action="store",
                    help="Number of nodes in one side of the dumbbell.",
                    required=True)
# Expt parameters
args = parser.parse_args()

class DumbbellTopo(Topo):
    "Dumbbell topology for Shrew experiment"
    def build(self, n=6, bw_net=100, delay='20ms', bw_host=10):
	#TODO:Add your code to create the topology.
	#Add 2 switches
	s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        self.addLink(s1, s2,bw=bw_net, delay=delay)

	#Left Side
	a1 = self.addHost('a1')
	hl1 = self.addHost('hl1')
	hl2 = self.addHost('hl2')
	# 10 Mbps, 20ms delay
        self.addLink(hl1, s1, bw=bw_net, delay=delay)
	self.addLink(hl2, s1, bw=bw_net, delay=delay)
	self.addLink(a1, s1, bw=bw_net, delay=delay)

	#Right Side
	a2 = self.addHost('a2')
	hr1 = self.addHost('hr1')
	hr2 = self.addHost('hr2')
	# 10 Mbps, 20ms delay
        self.addLink(hr1, s2, bw=bw_net, delay=delay)
	self.addLink(hr2, s2, bw=bw_net, delay=delay)
	self.addLink(a2, s2, bw=bw_net, delay=delay)

def bbnet():
    "Create network and run shrew  experiment"
    print "starting mininet ...."
    topo = DumbbellTopo(n=args.n, bw_net=args.bw_net,
                    delay='%sms' % (args.delay),
                    bw_host=args.bw_host)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink,
                  autoPinCpus=True)
    net.start()
    dumpNodeConnections(net.hosts)

    #TODO:Add your code to test reachability of hosts.
    print "Testing network connectivity"
    net.pingAll()
    
    #TODO:Add your code to start long lived TCP flows between
    #hosts on the left and right.
    print "Starting long lived tcp connection between hl1 and hr1, hl2 and hr2"
    hl1, hl2, hr1, hr2, a1 = net.get('hl1','hl2','hr1','hr2', 'a1')
    hl1_IP = hl1.IP()
    hl2_IP = hl2.IP()
    a1_IP = a1.IP()
    print a1_IP
    result = hl1.cmd('iperf -s &')
    result = hl2.cmd('iperf -s &')
    result = hr1.cmd('iperf -c' + hl1_IP + ' -t 120 &')
    result = hr2.cmd('iperf -c' + hl2_IP + ' -t 120 &')	
    #net.iperf((hI1, a2))	#check

    CLI(net)
    net.stop()

if __name__ == '__main__':
    bbnet()
