import networkx as nx
class Naive:
    def __init__(self,s,G):
        self.s=s
        self.G=G
        self.ans=[]
        self.l=[]
        self.mincost=9999999
        for i in G.nodes:
            if (i != s):
                self.l.append(i)
        self.solve()

    def permutation(self,lst):
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        l = []  #empty list that will store current permutation
        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i+1:]
            for p in self.permutation(remLst):
                l.append([m] + p)
        return l

    def solve(self):
        p= self.permutation(self.l)
        for a in p:
            temp=[]
            temp.append(self.s)
            prv=self.s
            t1=0
            for i in a:
                temp.append(i)
            temp.append(self.s)
            for nxt in temp:
                ed_dict=self.G.get_edge_data(prv,nxt)
                if ed_dict is None:
                    continue
                ed=ed_dict['weight']
                if(ed==0):
                    break
                t1+=ed
                prv=nxt
            if t1<self.mincost:
                self.mincost=t1
                self.ans=temp

    def getAns(self):
        return self.ans,self.mincost
