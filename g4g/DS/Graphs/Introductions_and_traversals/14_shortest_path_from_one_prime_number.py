''' Shortest path from one prime number to other by changing 1 digit '''

'''
   We generate an adjacency matrix of all prime number to 9999.
   Then we use BFS to find shortest path

   ** We use "Sieve of Eratosthenes" to generate the prime numbers
'''
from Queue import Queue
from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

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
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = visited[s] + 1
                    queue.append(i)
                if i == dest:
                    return visited[i] - 1

# 1033, 1733, 3733, 3739, 3779, 8779, 8179

def generate_prime():
    n = 9999
    prime = [True] * (n + 1)
    p = 2
    while p * p < n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Form a list of all prime number:
    prime_list = []
    for i in range(1000, n):
        if prime[i] == True:
            prime_list.append(i)
    return prime_list

def compare(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    count = 0
    if num1[0] != num2[0]:
        count += 1
    if num1[1] != num2[1]:
        count += 1 
    if num1[2] != num2[2]:
        count += 1
    if num1[3] != num2[3]:
        count += 1
    return count == 1

def shortest_path(src, dest):
    primeList = generate_prime()

    g = Graph(len(primeList))

    for i in range(len(primeList)):
        for j in range(i+1, len(primeList)):                    
            if compare(primeList[i], primeList[j]):
                g.add_edge(i, j)

    # Since graph nodes represent indexes of numbers in primeList
    # We need to find the index of src and dest
    for i in range(len(primeList)):
        if src == primeList[i]:
            src = i
        if dest == primeList[i]:
            dest = i

    return g.bfs(src, dest)

# 1033, 8179
# 3773, 3779
print shortest_path(1033, 8179)