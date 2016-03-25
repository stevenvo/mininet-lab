#!/usr/bin/python

"""
Create a network where different switches are connected to
different controllers, by creating a custom Switch() subclass.
"""

"""
TODO: Add two more controllers c3 and c4 which are default controllers. 
c3 controls s1 and s3. c4 controls s4. 
The remote controller (existing code) controls s2 only. 
Verify pingall is successfull.
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topolib import TreeTopo
from mininet.log import setLogLevel
from mininet.cli import CLI

setLogLevel( 'info' )

# Two local and one "external" controller (which is actually c0)
# Ignore the warning message that the remote isn't (yet) running
#c0 = Controller( 'c0', port=6633 )
#c1 = Controller( 'c1', port=6634 )
c2 = RemoteController( 'c2', ip='127.0.0.1' )
c3 = Controller( 'c3', port=6633 )
c4 = Controller( 'c4', port=6634 )

# cmap = { 's1': c0, 's2': c1, 's3': c2 }
cmap = { 's1': c3, 's2': c2, 's3':c3, 's4': c4 } # define the topo between controller to switch only

class MultiSwitch( OVSSwitch ):
    "Custom Switch() subclass that connects to different controllers"
    def start( self, controllers ):
        return OVSSwitch.start( self, [ cmap[ self.name ] ] )

topo = TreeTopo( depth=2, fanout=2 ) # define the topo between switch to switch, switch to host
net = Mininet( topo=topo, switch=MultiSwitch, build=False )
    
for c in [  c2, c3, c4 ]:
    net.addController(c)

net.build()
net.start() # invoking the MultiSwitch.start
print "*** Testing network"
net.pingAll()
CLI(net)
net.stop()
