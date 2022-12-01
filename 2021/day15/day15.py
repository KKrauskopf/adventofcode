from collections import defaultdict
from queue import PriorityQueue
import math

grid = []

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = defaultdict(str)
        self.visited = defaultdict(str)

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

def check_bounds(row, col):
    return row >= 0 and row <= len(grid)-1 and col >= 0 and col <= len(grid[0]) -1

def build_key(row, col):
    return str(row) + "," + str(col)

with open('/Users/krauskopf/projects/adventofcode/day15/input.txt') as f:
    for line in f.readlines():
        grid.append(list(map(int, list(line.strip()))))

graph = Graph(len(grid) * len(grid[0]))

for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        steps = [[1,0],[-1,0],[0,1],[0,-1]]
        old_key = build_key(row, col)
        for step in steps:
            new_row, new_col = row + step[0], col + step[1]
            new_key = build_key(new_row, new_col)
            if(check_bounds(new_row, new_col)):
                graph.add_edge(old_key,new_key,grid[new_row][new_col])
                graph.add_edge(new_key,old_key,grid[row][col])

print(graph)

# def dijkstra(graph, source):
#     dist = defaultdict(int)
#     previous = defaultdict(str)
#     for vertex in graph.keys():
#         dist[vertex] = math.inf
#         previous[vertex] = None
#     dist[source] = 0

#     pq = PriorityQueue()
#     pq.put((0,source))

#     while not pq.empty():
#         smalles_dist = min(dist, key=dist.get)
#         Q.remove(smalles_dist)
#         for neighbour in graph[smalles_dist]:
#             new_dist = dist[smalles_dist] + dist[neighbour]
#             if(new_dist < dist[neighbour]):
#                 dist[neighbour] = new_dist
#                 previous[neighbour] = smalles_dist
#     print(previous)


# dijkstra(graph, "0,0")
