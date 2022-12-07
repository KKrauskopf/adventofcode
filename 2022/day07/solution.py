commands = []

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.files = {}
        self.parent = None

with open('/Users/krauskopf/projects/adventofcode/2022/day07/input.txt') as f:
    command = []
    for line in f.readlines():
        if line.startswith("$") and len(command) > 0:
            commands.append(command.copy())
            command.clear()
        command.append(line.strip())
    commands.append(command.copy())
        
nodes = []
size_map = []

def solve1():
    score = 0
    build_nodes()
    for node in nodes:
        size = calculate_size(node)
        size_map.append(size)
    for entry in size_map:
        if entry <= 100000:
            score += entry
    print(score)

def solve2():
    max_space = 70000000
    needed_space = 30000000
    build_nodes()
    for node in nodes:
        size = calculate_size(node)
        size_map.append(size)
    
    free_space = max_space-max(size_map)
    need_to_free = needed_space - free_space

    size_map.sort()

    for entry in size_map:
        if entry >= need_to_free:
            print(entry)
            break


def calculate_size(node):
    size = 0
    for _, value in node.files.items():
        size += value
    for child in node.children:
        size += calculate_size(child)
    return size

def build_nodes():
    prev = None
    curr = None
    for command in commands:
        if "cd" in command[0]:
            if ".." in command[0]:
                curr = curr.parent
                continue
            prev = curr
            curr = Node(command[0].split(" ")[2])
            if prev is not None:
                prev.children.append(curr)
            curr.parent = prev
            nodes.append(curr)
        if "$ ls" in command[0]:
            for i in range(1, len(command)):
                if "dir " not in command[i]:
                    curr.files[command[i].split(" ")[1]] = int(command[i].split(" ")[0])

solve1()
solve2()
            