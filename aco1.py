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
        self.ans=[]
        self.cost = 9999999
        self.solve()

    def visitall(self,visit):
        for i in range(self.n):
            if visit[0, i] == 0:
                return False
        return True

    def solve(self):
        visibility = 1 / self.d
        visibility[visibility == inf] = 0

        # intializing pheromone present at the paths to the cities
        pheromone = np.ones((self.n, self.n))
        for i in range(self.n):
            pheromone[i, i] = 0
        # note adding 1 because we want to come back to the source city
        route = np.zeros((self.m, self.n + 1))
        for ite in range(self.iteration):
            for i in range(self.m):
                visit = np.zeros((1, self.n))
                route[i, 0] = i
                route[i, self.n] = i
                visit[0, i%self.n] = 1
                k = 1
                t4 = 0
                temp_visibility = np.array(visibility)  # creating a copy of visibility
                x = i%self.n
                while not (self.visitall(visit)):
                    t5 = 0
                    maxprob = 0
                    for y in range(self.n):
                        if visit[0, y] == 1 or y == x:
                            continue

                        t1 = pheromone[x%self.n, y]  # pheromone distribution b/w xny
                        t2 = temp_visibility[x%self.n, y]  # 1/d b/w xny
                        t3 = pow(t1, self.alpha) * pow(t2, self.beta)
                        if t3 > maxprob:
                            maxprob = t3
                            nextcity = y
                    x = nextcity
                    visit[0, x] = 1
                    route[i, k] = x
                    k += 1
                    t5 += t2
                t4 += t5
            # print(visibility)
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        continue
                    visibility[i, j] *= (1 - self.e)
                    visibility[i, j] += t4

        #print("route")
        #print(route)
        for ant in (route):
            prv = ant[0]
            temp_cost = 0
            for nxt in (ant):
                if nxt == prv:
                    continue
                prv = int(prv%self.n)
                nxt = int(nxt%self.n)
                temp_cost += self.d[prv, nxt]
                prv = nxt
            if temp_cost < self.cost:
                self.cost = temp_cost
                self.ans = ant

        #return cost

    def getAns(self):
        self.ans=[int(x) for x in self.ans]
        return self.ans, self.cost