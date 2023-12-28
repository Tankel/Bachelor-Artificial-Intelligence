import time
import random

class DSU:
    def __init__(self, N):
        self.leader = [0] * N
        self.rank = [0] * N

        for i in range(N):
            self.leader[i] = i

    def union(self, a, b):
        #Encontrar lider de a
        la = self.find(a)
        #Encontrar lider de b
        lb = self.find(b)
        #Hacer a padre de b
        self.leader[lb] = la

    def unionPC(self, a, b):
        #Encontrar lider de a con Path Compression
        la = self.pathCompression(a)
        #Encontrar lider de b con Path Compression
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

    def find(self, a):
        #Recorrer valores hasta que indice sea igual que valor
        if a == self.leader[a]:
            return self.leader[a]
        #Regresar el lider del conjunto
        return self.find(self.leader[a])
    
    def pathCompression(self, a):
        #Si el mismo a es el lider, regresamos a
        if a == self.leader[a]:
            return self.leader[a]
        
        #Si no, buscamos su lider y lo retornamos
        p = self.find(self.leader[a])
        self.leader[a] = p
        return p

naive = DSU(5000)
ubr = DSU(5000)
pc = DSU(5000)
opt = DSU(5000)

#Operaciones Naive
startTime = time.time()
for i in range(10000):
    operation = random.randint(0, 1)
    a = random.randint(0, 4999)
    if operation == 0:
        b = random.randint(0, 4999)
        naive.union(a, b)
    else:
        naive.find(a)
lapTime1 = time.time()
print("Tiempo Naive =", round((lapTime1 - startTime)*1000, 5), "milisegundos")

#Operaciones Union By Rank
for i in range(10000):
    operation = random.randint(0, 1)
    a = random.randint(0, 4999)
    if operation == 0:
        b = random.randint(0, 4999)
        ubr.unionByRank(a, b)
    else:
        ubr.find(a)
lapTime2 = time.time()
print("Tiempo con Union By Rank =", round((lapTime2 - lapTime1)*1000, 5), "milisegundos")

#Operaciones Path Compression
for i in range(10000):
    operation = random.randint(0, 1)
    a = random.randint(0, 4999)
    if operation == 0:
        b = random.randint(0, 4999)
        pc.unionPC(a, b)
    else:
        pc.find(a)
lapTime3 = time.time()
print("Tiempo Path Compression =", round((lapTime3 - lapTime2)*1000, 5), "milisegundos")

#Operaciones Optimal
for i in range(10000):
    operation = random.randint(0, 1)
    a = random.randint(0, 4999)
    if operation == 0:
        b = random.randint(0, 4000)
        opt.unionByRankPC(a, b)
    else:
        opt.find(a)
finalLap = time.time()
print("Tiempo Optimal =", round((finalLap - lapTime3)*1000, 5), "milisegundos")
