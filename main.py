from tkinter import *
from configs import SimulationConfig
from menu import MenuBar


class Application(Tk):
    def __init__(self):
        # Call the constructor of our parent class
        super().__init__()
        # Layout manager
        self.componentsFrame = Frame(self, width=512, height=500)
        self.componentsFrame.pack(fill=BOTH, side=LEFT, expand=True)

        self.formFrame = Frame(self, width=512, height=500)
        self.componentsFrame.pack(fill=BOTH, side=LEFT, expand=True)

        menu = MenuBar(self)
        menuBar = menu.setMenu()
        self.config(menu=menuBar)

        self.resetConfig()
        self.reloadComponentFrame()
        self.mininet = None

    def resetConfig(self):
        self.simulationConfig = SimulationConfig(None)

    def reloadComponentFrame(self):
        self.componentsFrame.pack_forget()
        self.componentsFrame = Frame(self, width=512, height=500)
        self.componentsFrame.pack(fill=BOTH, side=LEFT, expand=True)
        self.simulationConfig.setInFrame(self.componentsFrame)


if __name__ == "__main__":
    app = Application()
    app.title('POC integration Mininet')  # window title
    app.geometry('1024x500')  # default size
    # this loop allows for event-driven programming
    app.mainloop()