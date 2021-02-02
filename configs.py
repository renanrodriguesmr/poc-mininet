from tkinter import *
from tkinter.ttk import *

class LinkConfig:
    def __init__(self, linkForm):
        self.element1 = linkForm.element1.get()
        self.element2 = linkForm.element2.get()

    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='-------').grid(column = 0)
        Label(componentsFrame, text=(self.element1 + " - " + self.element2)).grid(column = 0)

class ControllerConfig:
    def __init__(self, controllerForm):
        self.name = controllerForm.name.get()
    
    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='-------').grid(column = 0)
        Label(componentsFrame, text=('name: ' + self.name)).grid(column = 0)

class HostConfig:
    def __init__(self, hostForm):
        self.name = hostForm.name.get()

    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='-------').grid(column = 0)
        Label(componentsFrame, text=('name: ' + self.name)).grid(column = 0)

class SwitchConfig:
    def __init__(self, switchForm):
        self.name = switchForm.name.get()

    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='-------').grid(column = 0)
        Label(componentsFrame, text=('name: ' + self.name)).grid(column = 0)

class APConfig:
    def __init__(self, apForm):
        self.name = apForm.name.get()
        self.ssid = apForm.ssid.get()
        self.mode = apForm.mode.get()
        self.channel = apForm.channel.get()
        self.mac = apForm.mac.get()
        self.ip = apForm.ip.get()
        self.position = apForm.position.get()
        self.range = apForm.range.get() # int

    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='-------').grid(columnspan=2)
        Label(componentsFrame, text=('name: ' + self.name)).grid(column = 0)
        Label(componentsFrame, text=('ssid: ' + self.ssid)).grid(column = 1)
        Label(componentsFrame, text=('mode: ' + self.mode)).grid(column = 0)
        Label(componentsFrame, text=('channel: ' + self.channel)).grid(column = 1)
        Label(componentsFrame, text=('mac: ' + self.mac)).grid(column = 0)
        Label(componentsFrame, text=('ip: ' + self.ip)).grid(column = 1)
        Label(componentsFrame, text=('position: ' + self.position)).grid(column = 0)
        Label(componentsFrame, text=('range: ' + str(self.range))).grid(column = 1)

class StationConfig:
    def __init__(self, stationForm):
        self.name = stationForm.name.get()
        self.min_x = stationForm.min_x.get()
        self.max_x = stationForm.max_x.get()
        self.min_y = stationForm.min_y.get()
        self.max_y = stationForm.max_y.get()
        self.min_v = stationForm.min_v.get()
        self.max_v = stationForm.max_v.get()
        self.bgscan_threshold = stationForm.bgscan_threshold.get()
        self.s_inverval = stationForm.s_inverval.get()
        self.l_interval = stationForm.l_interval.get()
        self.bgscan_module = stationForm.bgscan_module.get()

    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='-------').grid(columnspan=2)
        Label(componentsFrame, text=('name: ' + self.name)).grid(column = 0)
        Label(componentsFrame, text=('min_x: ' + str(self.min_x))).grid(column = 1)
        Label(componentsFrame, text=('max_x: ' + str(self.max_x))).grid(column = 0)
        Label(componentsFrame, text=('min_y: ' + str(self.min_y))).grid(column = 1)
        Label(componentsFrame, text=('max_y: ' + str(self.max_y))).grid(column = 0)
        Label(componentsFrame, text=('min_v: ' + str(self.min_v))).grid(column = 1)
        Label(componentsFrame, text=('max_v: ' + str(self.max_v))).grid(column = 0)
        Label(componentsFrame, text=('bgscan_threshold: ' + str(self.bgscan_threshold))).grid(column = 1)
        Label(componentsFrame, text=('s_inverval: ' + str(self.s_inverval))).grid(column = 0)
        Label(componentsFrame, text=('l_interval: ' + str(self.l_interval))).grid(column = 1)
        Label(componentsFrame, text=('bgscan_module: ' + self.bgscan_module)).grid(column = 0)

class NetworkConfig:
    def __init__(self, networkForm):
        self.name = networkForm.name.get()
        self.noise_th = networkForm.noise_th.get()
        self.fading_cof = networkForm.fading_cof.get()
        self.model = networkForm.model.get()
        self.exp = networkForm.exp.get()
    
    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text=('name: ' + self.name)).grid(column = 0)
        Label(componentsFrame, text=('noise_th: ' + str(self.noise_th))).grid(column = 0)
        Label(componentsFrame, text=('fading_cof: ' + str(self.fading_cof))).grid(column = 0)
        Label(componentsFrame, text=('model: ' + self.model)).grid(column = 0)
        Label(componentsFrame, text=('exp: ' + str(self.exp))).grid(column = 0)

class SimulationConfig:
    def __init__(self, networkConfig):
        self.network = networkConfig
        self.controllers = []
        self.hosts = []
        self.switches = []
        self.aps = []
        self.stations = []
        self.links = []

    def setInFrame(self, componentsFrame):
        Label(componentsFrame, text='============== Network =============').grid(columnspan=2)
        if self.network is not None:
            self.network.setInFrame(componentsFrame)
        
        Label(componentsFrame, text='============== Controllers =========').grid(columnspan=2)
        if self.controllers:
            for controller in self.controllers:
                controller.setInFrame(componentsFrame)

        Label(componentsFrame, text='============== Hosts ===============').grid(columnspan=2)
        if self.hosts:
            for host in self.hosts:
                host.setInFrame(componentsFrame)

        Label(componentsFrame, text='============== Switches ============').grid(columnspan=2)
        if self.switches:
            for switch in self.switches:
                switch.setInFrame(componentsFrame)

        Label(componentsFrame, text='============== Acess Points ========').grid(columnspan=2)
        if self.aps:
            for ap in self.aps:
                ap.setInFrame(componentsFrame)

        Label(componentsFrame, text='============== Stations ============').grid(columnspan=2)
        if self.stations:
            for station in self.stations:
                station.setInFrame(componentsFrame)

        Label(componentsFrame, text='============== Links ===============').grid(columnspan=2)
        if self.links:
            for link in self.links:
                link.setInFrame(componentsFrame)
