import time
import random

class DSU:
    def __init__(self, N):
        self.leader = [0] * N
        self.rank = [0] * N

        for i in range(N):
            self.leader[i] = i

    def printLeader(self):
        for i in range(self.leader.__len__()):
            print(self.leader[i], end = " ")

#---------------Metodos Union--------------------------------------------------

    def union(self, a, b):
        #Encontrar lider de a
        la = self.find(a)
        #Encontrar lider de b
        lb = self.find(b)
        #Hacer a padre de b
        self.leader[lb] = la

    def unionPC(self, a, b):
        #Encontrar lider de a
        la = self.pathCompression(a)
        #Encontrar lider de b
        lb = self.pathCompression(b)
        #Hacer a padre de b
        self.leader[lb] = la
    
    def unionByRank(self, a, b):
        #Encontrar lider de a
        la = self.find(a)
        #Encontrar lider de b
        lb = self.find(b)
        #Hacer a padre de b
        if self.rank[la] == self.rank[lb]:
            self.leader[la] = lb
            self.rank[lb] += 1
        elif self.rank[la] > self.rank[lb]:
            self.leader[lb] = la
        else:
            self.leader[la] = lb

    def unionByRankPC(self, a, b):
        #Encontrar lider de a
        la = self.pathCompression(a)
        #Encontrar lider de b
        lb = self.pathCompression(b)
        #Hacer a padre de b
        if self.rank[la] == self.rank[lb]:
            self.leader[la] = lb
            self.rank[lb] += 1
        elif self.rank[la] > self.rank[lb]:
            self.leader[lb] = la
        else:
            self.leader[la] = lb

    #------------Metodos Find-----------------------------------------------------


    def find(self, a):
        #Recorrer valores hasta que indice sea igual que valor
        if a == self.leader[a]:
            return self.leader[a]
        #Regresar el lider del conjunto
        return self.find(self.leader[a])
    
    def pathCompression(self, a):
        if a == self.leader[a]:
            return self.leader[a]
        
        p = self.find(self.leader[a])
        self.leader[a] = p
        return p
            

# Crear objetos de cada versión de Union Find
dsu_naive = DSU(5000)
dsu_rank = DSU(5000)
dsu_pc = DSU(5000)
dsu_optima = DSU(5000)

# Naive
start_time = time.time()
for i in range(10000):
    a = random.randint(0, 4999)
    if random.choice([True, False]):
        b = random.randint(0, 4999)
        dsu_naive.union(a, b)
    else:
        dsu_naive.find(a)
naive_time = time.time() - start_time

# UnionByRank
start_time = time.time()
for i in range(10000):
    a = random.randint(0, 4999)
    if random.choice([True, False]):
        b = random.randint(0, 4999)
        dsu_rank.unionByRank(a, b)
    else:
        dsu_rank.find(a)
rank_time = time.time() - start_time

# PathCompression
start_time = time.time()
for i in range(10000):
    a = random.randint(0, 4999)
    if random.choice([True, False]):
        b = random.randint(0, 4999)
        dsu_pc.unionPC(a, b)
    else:
        dsu_pc.find(a)
pc_time = time.time() - start_time

# Optima
start_time = time.time()
for i in range(10000):
    a = random.randint(0, 4999)
    if random.choice([True, False]):
        b = random.randint(0, 4999)
        dsu_optima.unionByRankPC(a, b)
    else:
        dsu_optima.find(a)
rank_pc_time = time.time() - start_time

'''
# Imprimimos los tiempos
print("Naive time:", round(naive_time*1000,4), end="ms\n")
print("UnionByRank time:", round(rank_time*1000,4), end="ms\n")
print("PathCompression time:", round(pc_time*1000,4), end="ms\n")
print("Optima (UnionByRank + PathCompression) time:", round(rank_pc_time*1000,4), end="ms\n")
'''