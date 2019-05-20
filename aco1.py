import networkx as nx
import numpy as np
from numpy import inf

class ACOSol:
    def __init__(self,G,n_ants,n_cities,it,alpha,beta,e):
        mat = []
        for i in G.nodes:
            t3 = []
            for j in G.nodes:
                ed_dict = G.get_edge_data(i, j)
                if ed_dict is None:
                    t3.append(0)
                else:
                    ed = ed_dict['weight']
                    t3.append(ed)
            mat.append(t3)
        self.d = np.array(mat)
        self.m=n_ants
        self.n=n_cities
        self.iteration=it
        self.alpha=alpha
        self.beta=beta
        self.e=e
        self.Visit_all = (1 << self.n) - 1
        self.ans=[]
        self.cost = 9999999
        self.solve()

    def solve(self):
        visibility = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    continue
                visibility[i, j] = 1 / self.d[i, j]
        # intializing pheromone present at the paths to the cities
        pheromone = np.full((self.n, self.n),10000)
        for i in range(self.n):
            pheromone[i, i] = 0
        # note adding 1 because we want to come back to the source city
        route = np.zeros((self.m, self.n + 1),dtype=np.uint16)
        for ite in range(self.iteration):
            update_pheromone = np.zeros((self.n, self.n))
            for i in range(self.m):
                route[i, 0] = i % self.n
                route[i, self.n] = i % self.n
                visit = 1 << (i % self.n)
                k = 1
                t4 = 0
                #temp_pheromone = np.array(pheromone)  # creating a copy of pheromone
                x = i % self.n
                #print("initially",i,visit)
                while not (visit==self.Visit_all):
                    maxprob = 0
                    for y in range(self.n):
                        #print(y,"\n")
                        if (visit&(1<<y)) or y == x:
                            continue
                        t1 = pheromone[x % self.n, y]  # pheromone distribution b/w xny
                        t2 = visibility[x % self.n, y]  # 1/d b/w xny
                        t3 = pow(t1, self.alpha) * pow(t2, self.beta)
                        #print(y,t3,"\n")
                        if t3 > maxprob :
                            maxprob = t3
                            nextcity = y
                    if x==nextcity:
                        for y in range(self.n):
                            if (not visit&(1<<y)) and y!=x:
                                nextcity=y
                    t4 += self.d[x, nextcity]
                    x = nextcity
                    visit |= 1 << x
                    #print(visit,"\nk",k,"x",x)
                    route[i, k] = x
                    k += 1
                x = i % self.n
                for z in (route[i]):
                    if x == z:
                        continue
                    #z=route[i,y]
                    #x=int(x)
                    #z=int(z)
                    update_pheromone[x, z] += 10000 / t4
                    update_pheromone[z, x] += 10000 / t4
                    x = z
            # print(pheromone)
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        continue
                    pheromone[i, j] *= (1 - self.e)
                    pheromone[i, j] += update_pheromone[i, j]

        for ant in (route):
            prv = ant[0]
            temp_cost = 0
            for nxt in (ant):
                if nxt == prv:
                    continue
                prv = int(prv % self.n)
                nxt = int(nxt % self.n)
                temp_cost += self.d[prv, nxt]
                prv = nxt
            if temp_cost < self.cost:
                self.cost = temp_cost
                self.ans = ant

        # return cost

    def getAns(self):
        self.ans=[int(x) for x in self.ans]
        return self.ans, self.cost