import networkx as nx

class DynamicSol:
    def __init__(self,s,G):
        self.s=s
        self.G=G
        self.citylist = {}
        self.ans = []
        self.ans.append(s)
        for i in G.nodes:
            self.citylist[i] = 0
        self.mincost(s)

    def least(self,city):
        ncity = 999999999
        minimum = 999999999
        for i in self.G.nodes:
            if i==self.s:
                continue
            if (self.citylist[i] == 0):
                ed_dict1 = self.G.get_edge_data(i, self.s)
                if ed_dict1 is None:
                    continue
                ed1 = ed_dict1['weight']
                ed_dict = self.G.get_edge_data(city, i)
                if ed_dict is None:
                    continue
                ed = ed_dict['weight']
                if ((ed+ed1) < minimum):
                    minimum = ed1 + ed
                    ncity = i
        return ncity

    def mincost(self,city):
        self.citylist[city] = 1
        nextcity = self.least(city)
        if (nextcity == 999999999):
            nextcity = self.s
            ed_dict = self.G.get_edge_data(city, nextcity)
            if ed_dict is None:
                return
            self.ans.append(nextcity)
            return
        else:
            self.ans.append(nextcity)
            self.mincost(nextcity)
        return

    def getans(self):
        return self.ans