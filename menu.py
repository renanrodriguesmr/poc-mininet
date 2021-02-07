from tkinter import Menu, Frame
from forms import LinkForm, NetworkForm, ControllerForm, HostForm, SwitchForm, APForm, StationForm
from mininetIntegration import Mininet

class MenuBar:
    def __init__(self, appplication):
        self.appplication = appplication

    def setMenu(self):
        menuBar = Menu(self.appplication)

        configMenu = Menu(menuBar, tearoff=0)
        configMenu.add_command(label="New Project", command=self._newProject)
        configMenu.add_separator()
        configMenu.add_command(label="Configure Network", command=self._newNetworkForm)
        configMenu.add_command(label="New Link", command=self._newLinkOption)
        configMenu.add_separator()
        configMenu.add_command(label="Run Project", command=self._run)
        configMenu.add_command(label="Stop Project", command=self._stop)
        menuBar.add_cascade(label="Configuration", menu=configMenu)

        componentMenu = Menu(menuBar, tearoff=0)
        componentMenu.add_command(label="New Station", command=self._newStationOption)
        componentMenu.add_command(label="New AcessPoint", command=self._newAPOption)
        componentMenu.add_separator()
        componentMenu.add_command(label="New Switch", command=self._newSwitchForm)
        componentMenu.add_command(label="New Host", command=self._newHostForm)
        componentMenu.add_command(label="New Controller", command=self._newControllerForm)
        menuBar.add_cascade(label="Components", menu=componentMenu)

        return menuBar

    def resetFormFrame(self):
        self.appplication.formFrame.grid_forget()
        self.appplication.formFrame = Frame()
        self.appplication.formFrame.grid(row=0, column=1)

    def _run(self):
        self.appplication.mininet = Mininet(self.appplication.simulationConfig)
        self.appplication.mininet.run()

    def _stop(self):
        if self.appplication.mininet is not None:
            self.appplication.mininet.stop()

    def _newProject(self):
        self.appplication.resetConfig()
        self.appplication.reloadComponentFrame()
    
    def _newNetworkForm(self):
        self._newForm(NetworkForm)

    def _newControllerForm(self):
        self._newForm(ControllerForm)

    def _newHostForm(self):
        self._newForm(HostForm)

    def _newSwitchForm(self):
        self._newForm(SwitchForm)

    def _newAPOption(self):
        self._newForm(APForm)

    def _newStationOption(self):
        self._newForm(StationForm)

    def _newLinkOption(self):
        self._newForm(LinkForm)

    def _newForm(self, Form):
        self.resetFormFrame()
        form = Form(self.appplication)
        form.createForm(self.appplication.formFrame)


