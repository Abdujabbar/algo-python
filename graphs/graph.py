__author__ = 'abdujabbor'


class Graph:
    def __init__(self, v):
        self.vertices = v
        self.edges = 0
        self.adj = [[0]*v]*v

    def __str__(self):
        return str(self.adj)

    def v(self):
        return self.vertices

    def e(self):
        return self.edges

    def add_edge(self, v, e):
        if self.adj[v][e] == 0:
            self.edges += 1
        self.adj[v][e] = 1


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
# #11000
# #01100
# #00100
# #10000
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
graph = {0: set([0, 1]),
         1: set([1, 2]),
         2: set([2]),
         3: set([]),
         }

print(list(bfs_paths(graph, 0, 2)))

# def has_next(a, i, j):


#11000
#01000
#01100
#10000
#
# n, m = [int(x) for x in input().split()]
#
# _max = max(n, m)
# _min = min(n, m)
# a = [0 * _min] * _max
#
# for i in range(_max):
#     a[i] = [int(x) for x in input().split()]
#
#
#
# if n > m:
#     vertices = n
#     t = m
# else:
#     vertices = m
#     t = n
# g = Graph(vertices)
# for i in range(vertices):
#     for j in range(t):
#         if a[i][j] == 1:
#             g.add_edge(i, j)
#
# for i in range(n):
#     f = Dfs(g, i)
#     print(f.count())
#

#
