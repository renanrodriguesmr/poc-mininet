from tkinter import *
from tkinter.ttk import *
from configs import LinkConfig, ControllerConfig, HostConfig, SwitchConfig, APConfig, StationConfig, NetworkConfig, SimulationConfig

class LinkForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.element1 = StringVar(self.appplication, '')
        self.element2 = StringVar(self.appplication, '')

    def createForm(self, formFrame):
        Label(formFrame, text='element 1: ').grid(row=0, column=0)
        Combobox(formFrame, values=self.getValues(), textvariable=self.element1).grid(row=0, column=1)

        Label(formFrame, text='element 2: ').grid(row=1, column=0)
        Combobox(formFrame, values=self.getValues(), textvariable=self.element2).grid(row=1, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=2, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=3, column=2)

    def getValues(self):
        values = []

        for host in self.appplication.simulationConfig.hosts:
            values.append(host.name)
        
        for switch in self.appplication.simulationConfig.switches:
            values.append(switch.name)
        
        for ap in self.appplication.simulationConfig.aps:
            values.append(ap.name)

        for station in self.appplication.simulationConfig.stations:
            values.append(station.name)

        return values

    def setInitialValues(self):
        self.element1.set('')
        self.element2.set('')


    def submit(self):
        link = LinkConfig(self)
        self.appplication.simulationConfig.links.append(link)
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

    def resetForm(self):
        self.setInitialValues()

class NetworkForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.name = StringVar(self.appplication, '')
        self.noise_th = IntVar(self.appplication, 0)
        self.fading_cof = IntVar(self.appplication, 0)
        self.model = StringVar(self.appplication, '')
        self.exp = IntVar(self.appplication, 0)

    def createForm(self, formFrame):
        Label(formFrame, text='name').grid(row=0, column=0)
        Entry(formFrame, textvariable=self.name).grid(row=0, column=1)

        Label(formFrame, text='noise_th').grid(row=1, column=0)
        Entry(formFrame, textvariable=self.noise_th).grid(row=1, column=1)

        Label(formFrame, text='fading_cof').grid(row=2, column=0)
        Entry(formFrame, textvariable=self.fading_cof).grid(row=2, column=1)

        Label(formFrame, text='model').grid(row=3, column=0)
        Entry(formFrame, textvariable=self.model).grid(row=3, column=1)

        Label(formFrame, text='exp').grid(row=4, column=0)
        Entry(formFrame, textvariable=self.exp).grid(row=4, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=5, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=6, column=2)

    def setInitialValues(self):
        self.name.set('')
        self.noise_th.set(0)
        self.fading_cof.set(0)
        self.model.set('')
        self.exp.set(0)


    def resetForm(self):
        self.setInitialValues()

    def submit(self):
        network = NetworkConfig(self)
        self.appplication.simulationConfig.network = network
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

class ControllerForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.name = StringVar(self.appplication, '')

    def createForm(self, formFrame):
        Label(formFrame, text='name').grid(row=0, column=0)
        Entry(formFrame, textvariable=self.name).grid(row=0, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=1, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=2, column=2)

    def setInitialValues(self):
        self.name.set('')


    def resetForm(self):
        self.setInitialValues()

    def submit(self):
        controller = ControllerConfig(self)
        self.appplication.simulationConfig.controllers.append(controller)
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

class HostForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.name = StringVar(self.appplication, '')

    def createForm(self, formFrame):
        Label(formFrame, text='name').grid(row=0, column=0)
        Entry(formFrame, textvariable=self.name).grid(row=0, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=1, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=2, column=2)

    def setInitialValues(self):
        self.name.set('')


    def resetForm(self):
        self.setInitialValues()

    def submit(self):
        host = HostConfig(self)
        self.appplication.simulationConfig.hosts.append(host)
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

class SwitchForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.name = StringVar(self.appplication, '')

    def createForm(self, formFrame):
        Label(formFrame, text='name').grid(row=0, column=0)
        Entry(formFrame, textvariable=self.name).grid(row=0, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=1, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=2, column=2)

    def setInitialValues(self):
        self.name.set('')


    def resetForm(self):
        self.setInitialValues()

    def submit(self):
        switch = SwitchConfig(self)
        self.appplication.simulationConfig.switches.append(switch)
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

class APForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.name = StringVar(self.appplication, '')
        self.ssid = StringVar(self.appplication, '')
        self.mode = StringVar(self.appplication, '')
        self.channel = StringVar(self.appplication, '')
        self.mac = StringVar(self.appplication, '')
        self.ip = StringVar(self.appplication, '')
        self.position = StringVar(self.appplication, '')
        self.range = IntVar(self.appplication, 0)

    def createForm(self, formFrame):
        Label(formFrame, text='name').grid(row=0, column=0)
        Entry(formFrame, textvariable=self.name).grid(row=0, column=1)

        Label(formFrame, text='ssid').grid(row=1, column=0)
        Entry(formFrame, textvariable=self.ssid).grid(row=1, column=1)

        Label(formFrame, text='mode').grid(row=2, column=0)
        Entry(formFrame, textvariable=self.mode).grid(row=2, column=1)

        Label(formFrame, text='channel').grid(row=3, column=0)
        Entry(formFrame, textvariable=self.channel).grid(row=3, column=1)

        Label(formFrame, text='mac').grid(row=4, column=0)
        Entry(formFrame, textvariable=self.mac).grid(row=4, column=1)

        Label(formFrame, text='ip').grid(row=5, column=0)
        Entry(formFrame, textvariable=self.ip).grid(row=5, column=1)

        Label(formFrame, text='position').grid(row=6, column=0)
        Entry(formFrame, textvariable=self.position).grid(row=6, column=1)

        Label(formFrame, text='range').grid(row=7, column=0)
        Entry(formFrame, textvariable=self.range).grid(row=7, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=8, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=9, column=2)

    def setInitialValues(self):
        self.name.set('')
        self.ssid.set('')
        self.mode.set('')
        self.channel.set('')
        self.mac.set('')
        self.ip.set('')
        self.position.set('')
        self.range.set(0)


    def resetForm(self):
        self.setInitialValues()

    def submit(self):
        ap = APConfig(self)
        self.appplication.simulationConfig.aps.append(ap)
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

class StationForm:
    def __init__(self, appplication):
        self.appplication = appplication
        self.name = StringVar(self.appplication, '')
        self.min_x = IntVar(self.appplication, 0)
        self.max_x = IntVar(self.appplication, 0)
        self.min_y = IntVar(self.appplication, 0)
        self.max_y = IntVar(self.appplication, 0)
        self.min_v = IntVar(self.appplication, 0)
        self.max_v = IntVar(self.appplication, 0)
        self.bgscan_threshold = IntVar(self.appplication, 0)
        self.s_inverval = IntVar(self.appplication, 0)
        self.l_interval = IntVar(self.appplication, 0)
        self.bgscan_module = StringVar(self.appplication, '')

    def createForm(self, formFrame):
        Label(formFrame, text='name').grid(row=0, column=0)
        Entry(formFrame, textvariable=self.name).grid(row=0, column=1)
        Label(formFrame, text='min_x').grid(row=1, column=0)
        Entry(formFrame, textvariable=self.min_x).grid(row=1, column=1)
        Label(formFrame, text='max_x').grid(row=2, column=0)
        Entry(formFrame, textvariable=self.max_x).grid(row=2, column=1)
        Label(formFrame, text='min_y').grid(row=3, column=0)
        Entry(formFrame, textvariable=self.min_y).grid(row=3, column=1)
        Label(formFrame, text='max_y').grid(row=4, column=0)
        Entry(formFrame, textvariable=self.max_y).grid(row=4, column=1)
        Label(formFrame, text='min_v').grid(row=5, column=0)
        Entry(formFrame, textvariable=self.min_v).grid(row=5, column=1)
        Label(formFrame, text='max_v').grid(row=6, column=0)
        Entry(formFrame, textvariable=self.max_v).grid(row=6, column=1)
        Label(formFrame, text='bgscan_threshold').grid(row=7, column=0)
        Entry(formFrame, textvariable=self.bgscan_threshold).grid(row=7, column=1)
        Label(formFrame, text='s_inverval').grid(row=8, column=0)
        Entry(formFrame, textvariable=self.s_inverval).grid(row=8, column=1)
        Label(formFrame, text='l_interval').grid(row=9, column=0)
        Entry(formFrame, textvariable=self.l_interval).grid(row=9, column=1)
        Label(formFrame, text='bgscan_module').grid(row=10, column=0)
        Entry(formFrame, textvariable=self.bgscan_module).grid(row=10, column=1)

        Button(formFrame, text ="submit", command = self.submit).grid(row=11, column=2)
        Button(formFrame, text ="reset", command = self.resetForm).grid(row=12, column=2)

    def setInitialValues(self):
        self.name.set('')
        self.min_x.set(0)
        self.max_x.set(0)
        self.min_y.set(0)
        self.max_y.set(0)
        self.min_v.set(0)
        self.max_v.set(0)
        self.bgscan_threshold.set(0)
        self.s_inverval.set(0)
        self.l_interval.set(0)
        self.bgscan_module.set('')

    def resetForm(self):
        self.setInitialValues()

    def submit(self):
        station = StationConfig(self)
        self.appplication.simulationConfig.stations.append(station)
        self.appplication.reloadComponentFrame()
        self.setInitialValues()

