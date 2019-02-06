from tkinter import *
from matplotlib import pyplot as plt
import networkx as nx
import math
import random as rd 
master =Tk()
Label(master,text="Enter no of nodes: ").grid(row=0)

e4=Entry(master)

e4.grid(row=0,column=1)


def draw_graph():
    
    G=nx.fast_gnp_random_graph(int(e4.get()),0.6)

    nx.draw_shell(G)
    plt.show()


def draw_graph2():
    n=int(e4.get())
    G=nx.Graph()
    for i in range(0,n):
        G.add_node(i+1)
#G=nx.complete_graph(n)
#G.remove_edges_from(G.edges())
    for i in range(0,n):
        for j in range(i+1,n):
            e1=rd.random()
            e2=rd.random()
            e3=rd.random()
            e=(int(e1*10)+int(e2*10))*(int(e3*10))
            if e!=0:
                G.add_weighted_edges_from([(i+1,j+1,e)])
#G.add_weighted_edges_from([(1,2,10),(1,3,14),(1,5,18),(2,3,7),(3,4,3),(3,5,11),(4,5,8)])
    pos = nx.circular_layout(G)
    nx.draw(G,pos, with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.draw()
    plt.show()


Button(master,text="Quit",command=quit).grid(row=3,column=0,sticky=W,pady=4)
Button(master,text="Draw",command=draw_graph2).grid(row=3,column=1,sticky=W,pady=4)
Button(master,text="Draw2",command=draw_graph).grid(row=3,column=2,sticky=W,pady=4)

mainloop()