from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.node import OVSKernelAP
from mn_wifi.node import UserAP
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference

class Mininet:
    def __init__(self, simulationConfig):
        self.config = simulationConfig

    def run(self):
        setLogLevel('info')
        self.topology()

    def topology(self):

        # Create a Network
        net = Mininet_wifi(controller=Controller, accessPoint=UserAP,
        link=wmediumd,wmediumd_mode=interference,
        noise_th=self.config.network.noise_th, fading_cof=self.config.network.fading_cof)

        # Creating Nodes
        nodeDict = {}
        for station in self.config.stations:
            nodeDict[station.name] = net.addStation(station.name, 
                                                    min_x=station.min_x, max_x=station.max_x, 
                                                    min_y=station.min_y, max_y=station.max_y, 
                                                    min_v=station.min_v, max_v=station.max_v,
                                                    bgscan_threshold=station.bgscan_threshold, 
                                                    s_inverval=station.s_inverval, 
                                                    l_interval=station.l_interval, 
                                                    bgscan_module=station.bgscan_module)

        
        for ap in self.config.aps:
            nodeDict[ap.name] = net.addAccessPoint(ap.name, 
                                              ssid=ap.ssid, mode=ap.mode, 
                                              channel=ap.channel, mac=ap.mac, 
                                              ip=ap.ip,position=ap.position, 
                                              range=ap.range)

        for switch in self.config.switches:
            nodeDict[switch.name] = net.addSwitch(switch.name)

        for host in self.config.hosts:
            nodeDict[host.name] = net.addHost(host.name)

        controllers = []
        for controller in self.config.controllers:
            c = net.addController(controller.name, controller=Controller)
            controllers.append(c)

        net.setPropagationModel(model=self.config.network.model, exp=self.config.network.exp)

        net.configureWifiNodes()

        for link in self.config.links:
            net.addLink(nodeDict[link.element1], nodeDict[link.element2])

        nodes = net.stations
        net.telemetry(nodes=nodes, single=True)
        net.build()

        for controller in controllers:
            controller.start()

        for key in nodeDict:
            nodeDict[key].start(controllers)

        
        CLI(net)

        net.stop()
