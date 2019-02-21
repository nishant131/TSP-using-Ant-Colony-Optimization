import networkx as nx
import matplotlib.pyplot as plt
import random as rd
%matplotlib inline

def least(city,const):
    const=const
    ncity=999999999
    minimum=999999999
    for i in G.nodes:
        ed_dict=G.get_edge_data(city,i)
        if ed_dict is None:
            continue
        ed=ed_dict['weight']
        if((citylist[i]==0)and(ed!=0)):
            if((2*ed)<minimum):
                ed_dict1=G.get_edge_data(i,const)
                if ed_dict1 is None:
                    continue
                ed1=ed_dict['weight']
                ed_dict2=G.get_edge_data(i,city)
                if ed_dict1 is None:
                    continue
                ed2=ed_dict['weight']
                minimum=ed1+ed2
                ncity=i
    return ncity

def mincost(city,const):
    const=const
    citylist[city]=1
    nextcity=least(city,const)
    if(nextcity==999999999):
        nextcity=const
        ed_dict=G.get_edge_data(city,nextcity)
        if ed_dict is None:
            return
        ed=ed_dict['weight']
        G1.add_weighted_edges_from([(city,nextcity,ed)])
        return
    else:
        nextcity
        ed_dict=G.get_edge_data(city,nextcity)
        ed=ed_dict['weight']
        G1.add_weighted_edges_from([(city,nextcity,ed)])
        mincost(nextcity,const)
    return

G=nx.Graph()
G1=nx.Graph()
n=input("Enter number of nodes:")
n=int(n)
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
#nx.draw_networkx_labels(G, pos, labels=None, font_size=18)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw_networkx_nodes(G, pos, node_color='b', node_size=700)
nx.draw_networkx_edges(G, pos, width=4, edge_color='r')
plt.draw()
plt.show()
print('\n')
for s in G.nodes:
    mincost(s,s)
    break;
pos = nx.circular_layout(G1)
nx.draw(G1,pos, with_labels=True)
labels = nx.get_edge_attributes(G1,'weight')
nx.draw_networkx_edge_labels(G1,pos,edge_labels=labels)
nx.draw_networkx_nodes(G1, pos, node_color='b', node_size=700)
nx.draw_networkx_edges(G1, pos, width=4, edge_color='r')
plt.draw()
plt.show()
