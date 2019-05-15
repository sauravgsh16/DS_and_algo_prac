''' Shortest path from one prime number to another '''

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def bfs(self, src, dest):
        visited = [0] * self.V
        queue = []
        queue.append(src)
        visited[src] = 1

        while len(queue) > 0:
            s = queue.pop(0)
            for i in range(len(self.graph[s])):
                if not visited[self.graph[s][i]]:
                    visited[self.graph[s][i]] = visited[s] + 1
                    queue.append(self.graph[s][i])
                if self.graph[s][i] == dest:
                    return visited[self.graph[s][i]] - 1


def generate_prime(n):
    p = 2
    prime = [True] * (n + 1)
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Create a prime_list
    primeList = []
    for i in range(1000, n):
        if prime[i] == True:
            primeList.append(i)
    return primeList


def compare(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    c = 0
    if n1[0] != n2[0]:
        c += 1
    if n1[1] != n2[1]:
        c += 1
    if n1[2] != n2[2]:
        c += 1
    if n1[3] != n2[3]:
        c += 1
    return c == 1

def shortest_path(src, dest):
    n = 9999
    primeList = generate_prime(n)

    g = Graph(len(primeList))

    for i in range(len(primeList)):
        for j in range(i + 1, len(primeList)):
            if compare(primeList[i], primeList[j]):
                g.add_edge(i, j)
    
    # Need to find index of src and dest
    for i in range(len(primeList)):
        if primeList[i] == src:
            src = i
        if primeList[i] == dest:
            dest = i
    
    return g.bfs(src, dest)


print shortest_path(1033, 8179)