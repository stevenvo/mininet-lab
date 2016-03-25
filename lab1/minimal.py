#!/usr/bin/python

from mininet.net import Mininet
# from mininet.util import createLink
net = Mininet()
# Crea:ng nodes in the network.
c0 = net.addController()
h0 = net.addHost('h0') 
s0 = net.addSwitch('s0')
h1 = net.addHost('h1')
# Creatingg links between nodes in network
net.addLink(h0, s0)
net.addLink(h1, s0)
# Configura:on of IP addresses in interfaces
h0.setIP('192.168.1.1', 24)
h1.setIP('192.168.1.2', 24)
net.start()
net.pingAll()
net.stop()

