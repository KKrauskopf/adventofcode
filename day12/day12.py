from collections import defaultdict

graph = defaultdict(list)

with open('/Users/krauskopf/projects/adventofcode/day12/input.txt') as f:
    for line in f.readlines():
        print(graph)
        source, target = line.split("-")
        source = source.strip()
        target = target.strip()
        if(source in graph):
            graph[source].append(target)
        else:
            graph[source] = [target]

        if(target in graph):
            graph[target].append(source)
        else:
            graph[target] = [source]

paths = []
def solve1(graph):
    print(graph)
    findPaths("start", [])
    print(len(paths))

def findPaths(node, visited):
    visited.append(node)
    for next in graph[node]:
        if next.islower() and next not in visited:
            findPaths(next, visited.copy())
        elif(next.isupper()):
            findPaths(next, visited.copy())
        else: continue
    if(node == "end"):
        paths.append(visited)
        return

solve1(graph)
