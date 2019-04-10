import networkx as nx
import numpy as np
import queue
import time

class Dynamic:
    def __init__(self,s,G,n):
        self.s=s
        self.G=G
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
        self.n=n
        self.ans = []
        self.ans.append(s)
        self.cost = 0
        self.Visit_all=(1<<n)-1
        self.dp = np.full(((2 ** n) + 2, n + 2), np.inf)
        self.dp1 = np.full(((2 ** n) + 2, n + 2), np.inf)
        self.cost=self.solve(1,self.s)
        self.travtime=0
        if n<10:
            tm1 = time.clock()
            self.find_path()
            tm2 = time.clock()
            self.travtime=tm2-tm1

    def solve(self,mask, pos):
        if mask == self.Visit_all:
            ed = self.d[self.s,pos]
            # print(pos,s,ed)
            self.dp[mask][pos] = ed
            self.dp1[mask][pos] = pos
            return ed
        mincost = 9999999

        for i in self.G.nodes:
            if (mask & (1 << i)) == 0:

                ed1 = self.d[i,pos]
                newcost = ed1 + self.solve(mask | (1 << i), i)
                if (self.dp[mask | (1 << i)][pos] > newcost):
                    self.dp[mask | (1 << i)][pos] = newcost
                    self.dp1[mask | (1 << i)][pos] = pos
                if newcost < mincost:
                    mincost = newcost
        return mincost

    def check(self,arr1):
        count1 = 0
        for i in range(2, len(arr1)):
            if arr1[i] > 0:
                count1 += 1
        return count1

    def find_path(self):
        L = queue.Queue(maxsize=1000000)
        arr = np.zeros(self.n + 2)
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
        L.put(arr)
        while not L.empty():
            arr1 = L.get()
            if (arr1[0] == self.s and arr1[1] == self.cost and self.check(arr1) == self.n):

                self.ans.append(0)
                nxt = 1
                while (nxt <= self.n):
                    for i in range(2, len(arr1)):
                        if (int(arr1[i]) == nxt):
                            self.ans.append(i - 2)
                            break
                    nxt += 1

            else:
                for i in self.G.nodes:
                    if arr1[0] != i and self.d[int(arr1[0]), i] != 0 and arr1[2 + i] == 0:
                        arr2 = np.copy(arr1)
                        arr2[0] = i
                        temp=int(arr1[0])
                        weight = self.d[temp, i]
                        arr2[1] = arr1[1] + weight

                        mx = -1
                        for j in range(2, len(arr1)):
                            mx = max(mx, arr1[j])
                        arr2[i + 2] = mx + 1
                        if (arr2[1] <= self.cost):
                            L.put(arr2)
        return

    def getans(self):
        return self.ans, self.cost