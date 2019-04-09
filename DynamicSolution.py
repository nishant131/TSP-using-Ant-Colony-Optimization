import networkx as nx

class Dynamic:
    def __init__(self,s,G):
        self.s=s
        self.G=G
        self.citylist = {}
        self.ans = []
        self.ans.append(s)
        for i in G.nodes:
            self.citylist[i] = 0
        self.cost = 0
        self.mincost(s)

    def least(self,city):
        ncity = 999999999
        minimum = 999999999
        for i in self.G.nodes:
            if i==self.s:
                continue
            ed_dict = self.G.get_edge_data(city, i)
            if ed_dict is None:
                continue
            ed = ed_dict['weight']
            if ((self.citylist[i] == 0) and (ed != 0)):
                if ((2*ed) < minimum):
                    ed_dict1 = self.G.get_edge_data(i, self.s)
                    if ed_dict1 is None:
                        continue
                    ed1 = ed_dict['weight']
                    ed_dict2 = self.G.get_edge_data(city,i)
                    if ed_dict2 is None:
                        continue
                    ed2 = ed_dict2['weight']
                    minimum = ed1 + ed2
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
            self.cost+=ed_dict['weight']
            return
        else:
            self.ans.append(nextcity)
            ed_dict = self.G.get_edge_data(city, nextcity)
            if ed_dict is None:
                return
            self.ans.append(nextcity)
            self.cost += ed_dict['weight']
            self.mincost(nextcity)
        return

    def getans(self):
        return self.ans, self.cost