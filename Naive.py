import networkx as nx

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

def naive(s, G):
    mn=99999999
    ans=[]
    l = []
    for i in G.nodes:
        if (i != s):
            l.append(i)
    p=permutation(l)
    for a in p:
        temp=[]
        temp.append(s)
        prv=s
        t1=0
        for i in a:
            temp.append(i)
        temp.append(s)
        for nxt in temp:
            ed_dict=G.get_edge_data(prv,nxt)
            if ed_dict is None:
                continue
            ed=ed_dict['weight']
            if(ed==0):
                break
            t1+=ed
            prv=nxt
        if t1<mn:
            mn=t1
            ans=temp
    return ans

'''for nxt in ans:
    ed_dict=G.get_edge_data(prv,nxt)
    if ed_dict is None:
        continue
    ed=ed_dict['weight']
    G1.add_weighted_edges_from([(prv,nxt,ed)])
    cost+=ed
    prv=nxt
'''