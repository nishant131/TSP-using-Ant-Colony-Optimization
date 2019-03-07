import matplotlib
matplotlib.use("TkAgg")

import random as rd

import matplotlib.pyplot as plt
import networkx as nx

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT=("Verdana",12)

#####################################################################################################

class drawGraph(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in (StartPage,PageTwo,PageThree,PageFour,PageFive):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

##################################################################################################

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Page2", command=lambda: controller.show_frame(PageTwo))
        button1.pack()
        button2 = ttk.Button(self, text="Page3", command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button3=ttk.Button(self, text="Page4", command=lambda: controller.show_frame(PageFour))
        button3.pack()
        button4 = ttk.Button(self, text="Page5", command=lambda: controller.show_frame(PageFive))
        button4.pack()
        button5 = ttk.Button(self, text="Quit", command=quit)
        button5.pack()

#############################################################################################

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

###############################################################################################

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

#######################################################################################################


##################################################################################################
class PageFive(tk.Frame):

    def __init__(self,parent,controller):
        ## LOGIC
        def least(city, const):
            const = const
            ncity = 999999999
            minimum = 999999999
            for i in G.nodes:
                ed_dict = G.get_edge_data(city, i)
                if ed_dict is None:
                    continue
                ed = ed_dict['weight']
                if ((citylist[i] == 0) and (ed != 0)):
                    if ((2 * ed) < minimum):
                        ed_dict1 = G.get_edge_data(i, const)
                        if ed_dict1 is None:
                            continue
                        ed1 = ed_dict['weight']
                        ed_dict2 = G.get_edge_data(i, city)
                        if ed_dict1 is None:
                            continue
                        ed2 = ed_dict['weight']
                        minimum = ed1 + ed2
                        ncity = i
            return ncity

        def mincost(city, const):
            const = const
            citylist[city] = 1
            nextcity = least(city, const)
            if (nextcity == 999999999):
                nextcity = const
                ed_dict = G.get_edge_data(city, nextcity)
                if ed_dict is None:
                    return
                ed = ed_dict['weight']
                G1.add_weighted_edges_from([(city, nextcity, ed)])
                return
            else:
                nextcity
                ed_dict = G.get_edge_data(city, nextcity)
                ed = ed_dict['weight']
                G1.add_weighted_edges_from([(city, nextcity, ed)])
                mincost(nextcity, const)
            return
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page4", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        #f = Figure(figsize=(5, 5), dpi=100)
        #a = f.add_subplot(111)
        #a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 6, 1, 2, 7, 4, 5])
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(211)
        #plt.axis('off')


        G=nx.Graph()
        G1=nx.Graph()
        #n=input("Enter number of nodes:")
        n=int(10)
        citylist={}
        for i in range(0,n):
            G.add_node(i)
            G1.add_node(i)
        for i in G.nodes:
            citylist[i]=0
        #G=nx.complete_graph(n)
        #G.remove_edges_from(G.edges())
        #arr=[[0,4,1,3],[4,0,2,1],[1,2,0,5],[3,1,5,0]]
        for i in range(0,n):
            for j in range(i+1,n):
                #e1=rd.random()
                #e2=rd.random()
                #e3=rd.random()
                #e=(int(e1*10)+int(e2*10))*(int(e3*10))
                e=rd.randrange(5,30,2)
                #e=arr[i][j]
                if e!=0:
                    G.add_weighted_edges_from([(i,j,e)])
        #G.add_weighted_edges_from([(1,2,10),(1,3,14),(1,5,18),(2,3,7),(3,4,3),(3,5,11),(4,5,8)])
        pos = nx.circular_layout(G)
        nx.draw(G,pos, with_labels=True)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_labels(G, pos, labels=None, font_size=12)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G, pos,  node_size=70)
        nx.draw_networkx_edges(G, pos, width=1)
        #plt.draw()
        #plt.show()
        #print('\n')
        for s in G.nodes:
            mincost(s,s)
            break
        plt.subplot(212)
        pos = nx.spectral_layout(G1)
        nx.draw(G1,pos, with_labels=True)
        labels = nx.get_edge_attributes(G1,'weight')
        nx.draw_networkx_edge_labels(G1,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G1, pos, node_size=70)
        nx.draw_networkx_edges(G1, pos, width=1)
        #plt.draw()
        #plt.show()

        xlim = a.get_xlim()
        ylim = a.get_ylim()
        # position is stored as node attribute data for random_geometric_graph

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




#######################################################################################################

class PageFour(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page3", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        #f = Figure(figsize=(5, 5), dpi=100)
        #a = f.add_subplot(111)
        #a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 6, 1, 2, 7, 4, 5])
        f = plt.figure(figsize=(8, 8))
        a = f.add_subplot(111)
        plt.axis('off')

        G = nx.complete_graph(20)
        pos = nx.circular_layout(G)

        nx.draw(G,pos)
        xlim = a.get_xlim()
        ylim = a.get_ylim()
        # position is stored as node attribute data for random_geometric_graph

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#######################################################################################################

app=drawGraph()
app.mainloop()