from tkinter import *
from tkinter.ttk import *
from configs import SimulationConfig
from menu import MenuBar


class Application(Tk):
    def __init__(self):
        # Call the constructor of our parent class
        super().__init__()
        # Layout manager
        self.componentsFrame = Frame(self)
        self.componentsFrame.grid(row=0, column=0)

        self.formFrame = Frame(self)
        self.formFrame.grid(row=0, column=1)

        menu = MenuBar(self)
        menuBar = menu.setMenu()
        self.config(menu=menuBar)

        self.resetConfig()
        self.reloadComponentFrame()

    def resetConfig(self):
        self.simulationConfig = SimulationConfig(None)

    def reloadComponentFrame(self):
        self.componentsFrame.grid_forget()
        self.componentsFrame = Frame()
        self.componentsFrame.grid(row=0, column=0)
        self.simulationConfig.setInFrame(self.componentsFrame)


if __name__ == "__main__":
    app = Application()
    app.title('POC integration Mininet')  # window title
    app.geometry('1024x500')  # window title
    # this loop allows for event-driven programming
    app.mainloop()