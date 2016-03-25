#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from  mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
# print "Single switch connected to  hosts.")
	def __init__(self, n=2, **opts):
		print("Initialize topology and default options")
		Topo.__init__(self, **opts)
		switch = self.addSwitch('s1')
		print("Python's range(N) generates 0..n")
		for h in range(n):
			host = self.addHost('h%s' % (h + 1))
			self.addLink(host, switch)

def simpleTest():
	print("Create and test a simple network")
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo)
	net.start()
	print ("Dumping host connections")
	dumpNodeConnections(net.hosts)
	print ("Testing network connectivity")
	net.pingAll()

	h1 = net.get('h1')
	ifconfig = h1.cmd('ifconfig')
	print(ifconfig)
	net.stop()

if __name__ == '__main__':
	print("Tell mininet to print useful information")
	setLogLevel('info')
	simpleTest()

