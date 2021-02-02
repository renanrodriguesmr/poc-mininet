from tkinter import *
from tkinter.ttk import *
from forms import LinkForm, NetworkForm, ControllerForm, HostForm, SwitchForm, APForm, StationForm

class MenuBar:
    def __init__(self, appplication):
        self.appplication = appplication

    def setMenu(self):
        menuBar = Menu(self.appplication)

        configMenu = Menu(menuBar, tearoff=0)
        configMenu.add_command(label="New Project", command=self.newProject)
        configMenu.add_separator()
        configMenu.add_command(label="Configure Network", command=self.newNetworkForm)
        configMenu.add_command(label="New Link", command=self.newLinkOption)
        configMenu.add_separator()
        configMenu.add_command(label="Run Project", command=self.run)
        menuBar.add_cascade(label="Configuration", menu=configMenu)

        componentMenu = Menu(menuBar, tearoff=0)
        componentMenu.add_command(label="New Station", command=self.newStationOption)
        componentMenu.add_command(label="New AcessPoint", command=self.newAPOption)
        componentMenu.add_separator()
        componentMenu.add_command(label="New Switch", command=self.newSwitchForm)
        componentMenu.add_command(label="New Host", command=self.newHostForm)
        componentMenu.add_command(label="New Controller", command=self.newControllerForm)
        menuBar.add_cascade(label="Components", menu=componentMenu)

        return menuBar

    def run(self):
        print("run")

    def newProject(self):
        self.appplication.resetConfig()
        self.appplication.reloadComponentFrame()

    def resetFormFrame(self):
        self.appplication.formFrame.grid_forget()
        self.appplication.formFrame = Frame()
        self.appplication.formFrame.grid(row=0, column=1)

    def donothing(self):
        self.resetFormFrame()
    
    def newNetworkForm(self):
        self.resetFormFrame()
        networkForm = NetworkForm(self.appplication)
        networkForm.createForm(self.appplication.formFrame)

    def newControllerForm(self):
        self.resetFormFrame()
        controllerForm = ControllerForm(self.appplication)
        controllerForm.createForm(self.appplication.formFrame)

    def newHostForm(self):
        self.resetFormFrame()
        hostForm = HostForm(self.appplication)
        hostForm.createForm(self.appplication.formFrame)

    def newSwitchForm(self):
        self.resetFormFrame()
        switchForm = SwitchForm(self.appplication)
        switchForm.createForm(self.appplication.formFrame)

    def newAPOption(self):
        self.resetFormFrame()
        apForm = APForm(self.appplication)
        apForm.createForm(self.appplication.formFrame)

    def newStationOption(self):
        self.resetFormFrame()
        stationForm = StationForm(self.appplication)
        stationForm.createForm(self.appplication.formFrame)

    def newLinkOption(self):
        self.resetFormFrame()
        linkForm = LinkForm(self.appplication)
        linkForm.createForm(self.appplication.formFrame)

