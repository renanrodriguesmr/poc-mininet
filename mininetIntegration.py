class Mininet:
    def __init__(self, simulationConfig):
        self.config = simulationConfig

    def run(self):
        print("\nnetwork")
        print(self.config.network.name)
        print(self.config.network.noise_th)
        print(self.config.network.fading_cof)
        print(self.config.network.model)
        print(self.config.network.exp)

        print("\ncontrollers")
        for controller in self.config.controllers:
            print("\n-------")
            print(controller.name)

        print("\nhosts")
        for host in self.config.hosts:
            print("\n-------")
            print(host.name)


        print("\nswitches")
        for switch in self.config.switches:
            print("\n-------")
            print(switch.name)

        print("\nacess points")
        for ap in self.config.aps:
            print("\n-------")
            print(ap.name)
            print(ap.ssid)
            print(ap.mode)
            print(ap.channel)
            print(ap.mac)
            print(ap.ip)
            print(ap.position)
            print(ap.range)

        print("\nstations")
        for station in self.config.stations:
            print("\n-------")
            print(station.name)
            print(station.min_x)
            print(station.max_x)
            print(station.min_y)
            print(station.max_y)
            print(station.min_v)
            print(station.max_v)
            print(station.bgscan_threshold)
            print(station.s_inverval)
            print(station.l_interval)
            print(station.bgscan_module)

        print("\nlinks")
        for link in self.config.links:
            print("\n-------")
            print(link.element1)
            print(link.element2)


