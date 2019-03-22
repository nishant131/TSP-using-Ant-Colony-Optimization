import networkx as nx
import matplotlib
import math
matplotlib.use("TkAgg")
import Naive as nv
import DynamicSolution as dsol
import aco1 as aco
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
        self.N = 5
        self.x = np.random.randint(1000, size=self.N)
        self.y = np.random.randint(1000, size=self.N)

        for i in range(0, self.N):
            self.G.add_node(i)
        for i in range(0, self.N):
            for j in range(0, self.N):
                if i == j:
                    continue
                else:
                    dist = math.sqrt((self.x[i] - self.x[j]) ** 2 + (self.y[i] - self.y[j]) ** 2)
                    self.G.add_weighted_edges_from([(i, j, dist)])


    def getNxy(self):
        return self.N, self.x, self.y
    def getgraph(self):
        return self.G
    def solve(self,s):
        return Naive.naive(s, self.G)

LARGE_FONT = ("Verdana", 12)
mg=MyGraph()
#####################################################################################################



#####################################################################################################

class drawGraph(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #mg = MyGraph()

        self.frames = {}
        for F in (StartPage,  PageSix, PageSeven, PageEight):
            frame = F(container,  self)
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
        button6 = ttk.Button(self, text="Naive", command=lambda: controller.show_frame(PageSix))
        button6.pack()
        button7 = ttk.Button(self, text="Dynamic Programming", command=lambda: controller.show_frame(PageSeven))
        button7.pack()
        button8 = ttk.Button(self, text="ACO", command=lambda: controller.show_frame(PageEight))
        button8.pack()
        button5 = ttk.Button(self, text="Quit", command=quit)
        button5.pack()
#######################################################################################################

class PageSix(tk.Frame,):
    def __init__(self, parent,  controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page6", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')



        N, x, y = mg.getNxy()
        tm1=time.clock()
        nvsol=nv.Naive(0,mg.getgraph())
        ans,cost = nvsol.getAns()
        tm2=time.clock()
        costLabel = tk.Label(self, text="Cost= "+str(cost), font=LARGE_FONT)
        costLabel.pack(pady=10, padx=10)
        timeLabel = tk.Label(self, text="Time= " + str(tm2-tm1), font=LARGE_FONT)
        timeLabel.pack(pady=10, padx=10)
        #print(cost)
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
    def __init__(self, parent,  controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page7", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')



        N,x,y=mg.getNxy()
        tm1=time.clock()
        ds= dsol.DynamicSol(0,mg.getgraph())
        tm2 = time.clock()
        ans=ds.getans()
        timeLabel = tk.Label(self, text="Time= " + str(tm2 - tm1), font=LARGE_FONT)
        timeLabel.pack(pady=10, padx=10)
        #print(ans)
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

class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page8", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')

        n_cities, x, y=mg.getNxy()
        n_ants = n_cities
        it = 50
        alpha = 0.85
        beta = 0.2
        e = 0.2
        tm1=time.clock()
        acosol= aco.ACOSol(mg.getgraph(), n_ants, n_cities, it, alpha, beta, e)
        tm2=time.clock()
        ans,cost = acosol.getAns()
        costLabel = tk.Label(self, text="Cost= " + str(cost), font=LARGE_FONT)
        costLabel.pack(pady=10, padx=10)
        timeLabel = tk.Label(self, text="Time= " + str(tm2 - tm1), font=LARGE_FONT)
        timeLabel.pack(pady=10, padx=10)

        #print(ans)
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