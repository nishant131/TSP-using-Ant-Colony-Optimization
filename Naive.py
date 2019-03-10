import networkx as nx
import matplotlib.pyplot as plt
import random as rd


def naive(s,l,G):
    mn=99999999
    ans=[]
    for a in l:
        temp=[]
        temp.append(s)
        prv=s
        t1=0
        for i in a:
            temp.append(i)
        for nxt in temp:
            if nxt==s:
                continue
            ed_dict=G.get_edge_data(prv,nxt)
            if ed_dict is None:
                continue
            ed=ed_dict['weight']
            if(ed==0):
                break
            t1+=ed
            prv=nxt
        ed_dict=G.get_edge_data(prv,s)
        if ed_dict is None:
            continue
        ed=ed_dict['weight']
        t1+=ed
        if t1<mn:
            mn=t1
            ans=temp
    ans.append(s)
    return ans
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []  #empty list that will store current permutation
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
G=nx.Graph()
G1=nx.Graph()
n=input("Enter number of nodes:")
n=int(n)
citylist={}
for i in range(0,n):
    G.add_node(i)
    G1.add_node(i)

for i in range(0,n):
    for j in range(i+1,n):
        e=rd.randrange(5,30,2)
        if e!=0:
            G.add_weighted_edges_from([(i,j,e)])
l=[]
for i in G.nodes:
    if(i!=0):
        l.append(i)
for i in G.nodes:
    s=i
    break
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
p=permutation(l)
ans=naive(s,p,G)
prv=s
for nxt in ans:
    if nxt==s:
        continue
    ed_dict=G.get_edge_data(prv,nxt)
    if ed_dict is None:
        continue
    ed=ed_dict['weight']
    G1.add_weighted_edges_from([(prv,nxt,ed)])
    prv=nxt
ed_dict=G.get_edge_data(prv,s)
ed=ed_dict['weight']
G1.add_weighted_edges_from([(prv,s,ed)])
pos = nx.circular_layout(G1)
nx.draw(G1,pos, with_labels=True)
labels = nx.get_edge_attributes(G1,'weight')
nx.draw_networkx_edge_labels(G1,pos,edge_labels=labels)
nx.draw_networkx_nodes(G1, pos, node_color='b', node_size=700)
nx.draw_networkx_edges(G1, pos, width=4, edge_color='r')
plt.draw()
plt.show()