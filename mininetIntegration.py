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
        self.__topology()

    def stop(self):
        self.net.stop()
        self.net = None

    def __topology(self):

        # Create a Network
        net = Mininet_wifi(controller=Controller, accessPoint=UserAP,
        link=wmediumd,wmediumd_mode=interference,
        noise_th=self.config.network.noise_th, fading_cof=self.config.network.fading_cof)

        for station in self.config.stations:
            net.addStation(
                station.name, 
                min_x=station.min_x, max_x=station.max_x, 
                min_y=station.min_y, max_y=station.max_y, 
                min_v=station.min_v, max_v=station.max_v,
                bgscan_threshold=station.bgscan_threshold, 
                s_inverval=station.s_inverval, 
                l_interval=station.l_interval, 
                bgscan_module=station.bgscan_module
            )

        # Creating Nodes
        nodeDict = {}
        for apConfig in self.config.aps:
            ap = net.addAccessPoint(
                apConfig.name, 
                ssid=apConfig.ssid, mode=apConfig.mode, 
                channel=apConfig.channel, mac=apConfig.mac, 
                ip=apConfig.ip,position=apConfig.position, 
                range=apConfig.range
            )
            
            nodeDict[apConfig.name] = {
                'value': ap,
                'type': 'acess_point'
            }

        for switchConfig in self.config.switches:
            switch = net.addSwitch(switchConfig.name)
            nodeDict[switchConfig.name] = {
                'value': switch,
                'type': 'switch'    
            }
            

        for hostConfig in self.config.hosts:
            host = net.addHost(hostConfig.name)
            nodeDict[hostConfig.name] = {
                'value': host,
                'type': 'host'    
            }

        controllers = []
        for controller in self.config.controllers:
            c = net.addController(controller.name, controller=Controller)
            controllers.append(c)

        net.setPropagationModel(model=self.config.network.model, exp=self.config.network.exp)

        net.configureWifiNodes()

        for link in self.config.links:
            net.addLink(nodeDict[link.element1]['value'], nodeDict[link.element2]['value'])

        nodes = net.stations
        net.telemetry(nodes=nodes, single=True)
        net.build()

        for controller in controllers:
            controller.start()

        for key in nodeDict:
            if(nodeDict[key]['type'] != 'host'):
                nodeDict[key]['value'].start(controllers)

        self.net = net
        CLI(net)
        self.stop()
