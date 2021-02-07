from tkinter import *
from configs import SimulationConfig
from menu import MenuBar


class Application(Tk):
    def __init__(self):
        # Call the constructor of our parent class
        super().__init__()
        # Layout manager

        self.scrollableArea = Frame(self, width=512, height=500)
        self.scrollableArea.pack(fill=BOTH,side=LEFT, expand=1)
        self.myCanvas = Canvas(self.scrollableArea)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrollY = Scrollbar(self.scrollableArea, orient=VERTICAL, command=self.myCanvas.yview)
        self.scrollY.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand = self.scrollY.set)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion = self.myCanvas.bbox("all")))
        self.componentsFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.componentsFrame, anchor="nw")
        
        self.formFrame = Frame(self, width=512, height=500)
        self.formFrame.pack(fill=BOTH, side=RIGHT, expand=True)

        menu = MenuBar(self)
        menuBar = menu.setMenu()
        self.config(menu=menuBar)

        self.resetConfig()
        self.reloadComponentFrame()
        self.mininet = None

    def resetConfig(self):
        self.simulationConfig = SimulationConfig(None)

    def reloadComponentFrame(self):
        self.scrollableArea.pack_forget()

        self.scrollableArea = Frame(self, width=512, height=500)
        self.scrollableArea.pack(fill=BOTH,side=LEFT, expand=1)
        self.myCanvas = Canvas(self.scrollableArea)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrollY = Scrollbar(self.scrollableArea, orient=VERTICAL, command=self.myCanvas.yview)
        self.scrollY.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand = self.scrollY.set)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion = self.myCanvas.bbox("all")))
        self.componentsFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.componentsFrame, anchor="nw")

        self.simulationConfig.setInFrame(self.componentsFrame)


if __name__ == "__main__":
    app = Application()
    app.title('POC integration Mininet')  # window title
    app.geometry('1024x500')  # default size
    # this loop allows for event-driven programming
    app.mainloop()