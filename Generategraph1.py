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
from tkinter import *


class MyGraph:
    def __init__(self,N):
        self.G=nx.Graph()
        self.N = N
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


LARGE_FONT = ("Verdana", 12)
#mg=MyGraph()
#####################################################################################################
#####################################################################################################

class drawGraph(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        #mg = MyGraph()

        self.frames = {}
        for F in (StartPage,):
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
        self.parent=parent
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self.parent, text="Start Page", font=LARGE_FONT)
        label.grid(row=3, column=1,sticky="nsew")
        inputlab = tk.Label(self.parent, text="Enter number of nodes")
        inputlab.grid(row=4, column=0,sticky="nsew")
        self.T = Entry(parent)
        self.T.grid(row=4, column=1,sticky="nsew")
        gengraph = ttk.Button(self.parent, text="Generate Graph", command=self.displayGraph)
        gengraph.grid(row=5, column=1,sticky="nsew")
        self.N=None
        '''button7 = ttk.Button(self, text="Page7", command=lambda: controller.show_frame(PageSeven))
        button7.grid()
        button5 = ttk.Button(self, text="Quit", command=quit)
        button5.grid()'''

    def displayGraph(self):
        if self.N is None:
            self.N = self.T.get()
            self.T.destroy()
            self.N = int(self.N)
            self.mg = MyGraph(self.N)
            self.N, self.x, self.y = self.mg.getNxy()


        for child in self.parent.winfo_children():
            child.destroy()

        label = tk.Label(self.parent, text="Random Graph", font=LARGE_FONT)
        label.grid(row=1, column=1)
        naivebutton = ttk.Button(self.parent, text="Naive", command=self.naivesol)
        naivebutton.grid(row=3, column=0 )
        dpbutton = ttk.Button(self.parent, text="Dynamic Programming",command=self.dpsol)
        dpbutton.grid(row=3, column=1)
        acobutton = ttk.Button(self.parent, text="ACO", command=self.inputACO)
        acobutton.grid(row=3, column=2)
        #button1 = ttk.Button(self, text="Back to Home", command=app.mainloop)
        #button1.grid()
        quitbutton = Button(self.parent, text="Quit", command=quit)
        quitbutton.grid(row=4, column=1)

        f = plt.figure(figsize=(9, 5))
        a = f.add_subplot(111)
        colors = ("black")
        area = np.pi * 3
        # Plot
        plt.scatter(self.x, self.y, s=area, c=colors, alpha=0.5)
        # splt.title('Scatter plot pythonspot.com')
        plt.xlabel('x')
        plt.ylabel('y')
        # plt.show()

        xlim = a.get_xlim()
        ylim = a.get_ylim()
        fr = tk.Frame(self.parent)
        fr.grid(row=5, column=3, rowspan=1,columnspan=4)


        canvas = FigureCanvasTkAgg(f, master=fr)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, fr)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #######################################################################################################
    def plotsol(self,ans):
        f = plt.figure(figsize=(9, 5))
        a = f.add_subplot(111)
        # plt.axis('off')
        colors = ("black")
        area = np.pi * 3
        # Plot
        plt.scatter(self.x, self.y, s=area, c=colors, alpha=0.5)
        x1 = []
        y1 = []
        # ind=0
        for i in (ans):
            x1.append(self.x[i])
            y1.append(self.y[i])
            # ind+=1
        plt.plot(x1, y1, c=colors, alpha=0.5)
        # splt.title('Scatter plot pythonspot.com')
        plt.xlabel('x')
        plt.ylabel('y')
        # plt.show()
        xlim = a.get_xlim()
        ylim = a.get_ylim()
        fr = tk.Frame(self.parent)
        fr.grid(row=5, column=3, rowspan=1, columnspan=4)
        canvas = FigureCanvasTkAgg(f, master=fr)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, fr)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def naivesol(self):
            for child in self.parent.winfo_children():
                child.destroy()
            # tk.Frame.__init__(self, parent)
            label = tk.Label(self.parent, text="Naive", font=LARGE_FONT)
            label.grid(row=0 , column=1)
            #button1 = ttk.Button(self, text="Back to Home", command=self.__init__)
            #button1.grid()
            backbutton = ttk.Button(self.parent, text="Back to Graph", command=self.displayGraph)
            backbutton.grid()
            if (self.N >= 12):
                label1 = tk.Label(self.parent, text="Nodes exceeded", font=LARGE_FONT)
                label1.grid(row=1 , column=1)
            else:
                tm1 = time.clock()
                nvsol = nv.Naive(0, self.mg.getgraph())
                tm2 = time.clock()
                ans, cost = nvsol.getAns()
                costLabel = tk.Label(self.parent, text="Cost= " + str(cost), font=LARGE_FONT)
                costLabel.grid(row=1 , column=1)
                timeLabel = tk.Label(self.parent, text="Time= " + str(tm2 - tm1), font=LARGE_FONT)
                timeLabel.grid(row=2 , column=1)
                # print(cost)
                self.plotsol(ans)

    #######################################################################################################

    def dpsol(self):
        for child in self.parent.winfo_children():
            child.destroy()
        label = tk.Label(self.parent, text="Dynamic Programming", font=LARGE_FONT)
        label.grid(row=0 , column=1)
        #button1 = ttk.Button(self, text="Back to Home", command=lambda: self.controller.show_frame(StartPage))
        #button1.grid()
        backbutton = ttk.Button(self.parent, text="Back to Graph", command=self.displayGraph)
        backbutton.grid(row=3 , column=1)
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')
        tm1 = time.clock()
        ds = dsol.Dynamic(0, self.mg.getgraph())
        tm2 = time.clock()
        ans, cost = ds.getans()
        costLabel = tk.Label(self.parent, text="Cost= " + str(cost), font=LARGE_FONT)
        costLabel.grid(row= 1, column=1)
        timeLabel = tk.Label(self.parent, text="Time= " + str(tm2 - tm1), font=LARGE_FONT)
        timeLabel.grid(row= 2, column=1)
        self.plotsol(ans)

    def inputACO(self):
        for child in self.parent.winfo_children():
            child.destroy()
        label = tk.Label(self.parent, text="Input Parameters", font=LARGE_FONT)
        label.grid(row=0, column=1)
        label1 = tk.Label(self.parent, text="Number of ants:", font=LARGE_FONT)
        label1.grid(row= 1, column=0)
        self.T1 = Entry(self.parent)
        self.T1.grid(row= 1, column=1)
        label2 = tk.Label(self.parent, text="Number of Iterations:", font=LARGE_FONT)
        label2.grid(row=2 , column=0)
        self.T2 = Entry(self.parent)
        self.T2.grid(row=2 , column=1)
        label3= tk.Label(self.parent, text="Alpha:", font=LARGE_FONT)
        label3.grid(row= 3, column=0)
        self.T3 = Entry(self.parent)
        self.T3.grid(row= 3, column=1)
        label4= tk.Label(self.parent, text="Beta:", font=LARGE_FONT)
        label4.grid(row=4 , column=0)
        self.T4 = Entry(self.parent)
        self.T4.grid(row=4 , column=1)
        label5= tk.Label(self.parent, text="Visibility Constant:", font=LARGE_FONT)
        label5.grid(row=5 , column=0)
        self.T5 = Entry(self.parent)
        self.T5.grid(row=5 , column=1)
        button = ttk.Button(self.parent, text="Solve", command=self.acosol)
        button.grid(row=6,column=1)

    def acosol(self):
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        # plt.axis('off')
        n_cities, x, y = self.mg.getNxy()
        n_ants = int(self.T1.get())
        it = int(self.T2.get())
        alpha = float(self.T3.get())
        beta = float(self.T4.get())
        e = float(self.T5.get())
        tm1 = time.clock()
        acosol = aco.ACOSol(self.mg.getgraph(), n_ants, n_cities, it, alpha, beta, e)
        tm2 = time.clock()
        ans, cost = acosol.getAns()
        for child in self.parent.winfo_children():
            child.destroy()
        label = tk.Label(self.parent, text="ACO", font=LARGE_FONT)
        label.grid(row=0, column=1)
        # button1 = ttk.Button(self, text="Back to Home", command= self.controller.show_frame(StartPage))
        # button1.grid()
        backbutton = ttk.Button(self.parent, text="Back to Graph", command=self.displayGraph)
        backbutton.grid(row=4, column=1)
        backbutton1 = ttk.Button(self.parent, text="Change ACO Parameters", command=self.inputACO)
        backbutton1.grid(row=3, column=1)
        costLabel = tk.Label(self.parent, text="Cost= " + str(cost), font=LARGE_FONT)
        costLabel.grid(row=1 , column=1)
        timeLabel = tk.Label(self.parent, text="Time= " + str(tm2 - tm1), font=LARGE_FONT)
        timeLabel.grid(row=2 , column=1)
        # print(ans)
        self.plotsol(ans)