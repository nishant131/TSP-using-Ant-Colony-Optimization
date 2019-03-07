import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import networkx as nx

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT=("Verdana",12)

class drawGraph(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in (StartPage,PageTwo,PageThree):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Page2", command=lambda: controller.show_frame(PageTwo))
        button1.pack()
        button2 = ttk.Button(self, text="Page3", command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button3=ttk.Button(self, text="Quit", command=quit)
        button3.pack()

class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Page2",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1=ttk.Button(self,text="Back to Home",command=lambda :controller.show_frame(StartPage))
        button1.pack()
        f=Figure(figsize=(5,5),dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,3,6,1,2,7,4,5])

        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()

        toolbar=NavigationToolbar2Tk(canvas,self)
        toolbar.update()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        #f = Figure(figsize=(5, 5), dpi=100)
        #a = f.add_subplot(111)
        #a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 6, 1, 2, 7, 4, 5])
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        plt.axis('off')

        G = nx.random_geometric_graph(200, 0.125)
        pos = nx.get_node_attributes(G, 'pos')

        # find node near center (0.5,0.5)
        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - 0.5) ** 2 + (y - 0.5) ** 2
            if d < dmin:
                ncenter = n
                dmin = d

        # color by path length from node near center
        p = dict(nx.single_source_shortest_path_length(G, ncenter))

        #plt.figure(figsize=(8, 8))
        nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
        nx.draw_networkx_nodes(G, pos, nodelist=list(p.keys()),
                               node_size=80,
                               node_color=list(p.values()),
                               cmap=plt.cm.Reds_r)
        xlim = a.get_xlim()
        ylim = a.get_ylim()
        # position is stored as node attribute data for random_geometric_graph

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app=drawGraph()
app.mainloop()