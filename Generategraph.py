import networkx as nx
import matplotlib
import math
matplotlib.use("TkAgg")
import Naive
import DynamicSolution as dsol
import time
import random as rd

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
import numpy as np
from tkinter import ttk

class MyGraph:
    def __init__(self):
        self.G=nx.Graph()
    def generategraph(self,N,x,y):
        for i in range(0, N):
            self.G.add_node(i)
        for i in range(0, N):
            for j in range(0, N):
                if i == j:
                    continue
                else:
                    dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
                    self.G.add_weighted_edges_from([(i, j, dist)])
        return
    def getgraph(self):
        return self.G
    def solve(self,s):
        return Naive.naive(s, self.G)

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
        for F in (StartPage,  PageSix, PageSeven):
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
        button7 = ttk.Button(self, text="Page7", command=lambda: controller.show_frame(PageSeven))
        button7.pack()
        button5 = ttk.Button(self, text="Quit", command=quit)
        button5.pack()
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
        N = 5
        x = np.random.randint(1000,size=N)
        y = np.random.randint(1000,size=N)

        mg = MyGraph()
        mg.generategraph(N, x, y)
        ans = mg.solve(0)
        colors = ("black")
        area = np.pi * 3
        # Plot
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        x1=[]
        y1=[]
        #ind=0
        for i in (ans):
            x1.append(x[i])
            y1.append(y[i])
            #ind+=1
        plt.plot(x1, y1, c=colors, alpha=0.5)
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

class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page7", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')
        N = 20
        x = np.random.randint(1000,size=N)
        y = np.random.randint(1000,size=N)

        mg = MyGraph()
        mg.generategraph(N, x, y)
        ds= dsol.DynamicSol(0,mg.getgraph())
        ans=ds.getans()
        print(ans)
        colors = ("black")
        area = np.pi * 3
        # Plot
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        x1=[]
        y1=[]
        #ind=0
        for i in (ans):
            x1.append(x[i])
            y1.append(y[i])
            #ind+=1
        plt.plot(x1, y1, c=colors, alpha=0.5)
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
