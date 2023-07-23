
from mininet.topo import Topo

class MyTopo( Topo ):
    "8 switch 8 host custom topology"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )

        # Add links
        self.addLink( h1, s1 ,bw=1000, delay='1ms')
        self.addLink( h2, s2 ,bw=1000, delay='1ms')
        self.addLink( h3, s3 ,bw=1000, delay='1ms')
        self.addLink( h4, s4 ,bw=1000, delay='1ms')
        self.addLink( h5, s5 ,bw=1000, delay='1ms')
        self.addLink( h6, s6 ,bw=1000, delay='1ms')
        self.addLink( h7, s7 ,bw=1000, delay='1ms')
        self.addLink( h8, s8 ,bw=1000, delay='1ms')

        self.addLink( s1, s3 ,bw=1000, delay='1ms')
        self.addLink( s1, s8 ,bw=1000, delay='1ms')
        self.addLink( s2, s4 ,bw=1000, delay='1ms')
        self.addLink( s2, s5 ,bw=1000, delay='1ms')
        self.addLink( s2, s7 ,bw=1000, delay='1ms')
        self.addLink( s3, s4 ,bw=1000, delay='1ms')
        self.addLink( s3, s6 ,bw=1000, delay='1ms')
        self.addLink( s3, s8 ,bw=1000, delay='1ms')
        self.addLink( s4, s5 ,bw=1000, delay='1ms')
        self.addLink( s4, s7 ,bw=1000, delay='1ms')
        self.addLink( s5, s6 ,bw=1000, delay='1ms')
        self.addLink( s5, s7 ,bw=1000, delay='1ms')
        self.addLink( s6, s8 ,bw=1000, delay='1ms')
        self.addLink( s7, s8 ,bw=1000, delay='1ms')
 

        

topos = { 'mytopo': ( lambda: MyTopo() ) }
