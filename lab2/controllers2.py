#!/usr/bin/python

"""
This example creates a multi-controller network from semi-scratch by
using the net.add*() API and manually starting the switches and controllers.

This is the "mid-level" API, which is an alternative to the "high-level"
Topo() API which supports parametrized topology classes.

Note that one could also create a custom switch class and pass it into
the Mininet() constructor.

TODO:  tree topology with 3 switches and 4 hosts
s1<-->s2 s1<-->s3 c1<-->s1 c2<-->s2 c3<-->s3  s2<-->h1 s2<-->h2 s3<-->h3 s3<-->h4
"""

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=Controller, switch=OVSSwitch )

    print "*** Creating (reference) controllers"
    c1 = net.addController( 'c1', port=6633 )
    c2 = net.addController( 'c2', port=6634 )
    c3 = net.addController( 'c3', port=6635 )

    print "*** Creating switches"
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )

    print "*** Creating hosts"
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    
    print "*** Creating links"
    net.addLink(s1,s2) #s1 <-> s2
    net.addLink(s1,s3) #s1 <-> s3
    
    net.addLink(s2,h1) #s2 <-> h1
    net.addLink(s2,h2) #s2 <-> h2
    
    net.addLink(s3,h3) #s3 <-> h3
    net.addLink(s3,h4) #s3 <-> h4

    print "*** Starting network"
    net.build()
    c1.start()
    c2.start()
    c3.start()
    s1.start( [ c1 ] )
    s2.start( [ c2 ] )
    s3.start( [ c3 ] )

    print "*** Testing network"
    net.pingAll()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()
