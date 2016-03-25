#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from  mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):

    # print "Single switch connected to  hosts.")
    def __init__(self, n=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)
            # host.cmd('ifconfig')

    def execute_command(self, net, command):
        print "EXECUTE COMMAND: {} on all hosts".format(command)
        for h in self.hosts():
            host = net.get(h)
            # host.cmd(command)
            print "HOST {0}:\n{1}\n\n".format(h, host.cmd(command))

def simpleTest():
    # "Create and test a simple network"
    topo = SingleSwitchTopo(4)
    net = Mininet(topo)
    net.start()
    topo.execute_command(net, 'ifconfig')
    print ("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print ("Testing network connectivity")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    # setLogLevel('info')
    simpleTest()

