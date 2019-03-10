import matplotlib

matplotlib.use("TkAgg")

import time
import random as rd

import matplotlib.pyplot as plt
import networkx as nx

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
import numpy as np
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


#####################################################################################################

class drawGraph(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,  PageSix):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


##################################################################################################

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button6 = ttk.Button(self, text="Page6", command=lambda: controller.show_frame(PageSix))
        button6.pack()
        button5 = ttk.Button(self, text="Quit", command=quit)
        button5.pack()


#############################################################################################



###############################################################################################



#######################################################################################################


##################################################################################################


#######################################################################################################



#######################################################################################################

class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page6", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')
        N = 20
        x = np.random.randint(1000,size=N)
        y = np.random.randint(1000,size=N)
        colors = ("black")
        area = np.pi * 3

        # Plot
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        # splt.title('Scatter plot pythonspot.com')
        plt.xlabel('x')
        plt.ylabel('y')
        # plt.show()

        xlim = a.get_xlim()
        ylim = a.get_ylim()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = drawGraph()
app.geometry("1280x720")
app.mainloop()