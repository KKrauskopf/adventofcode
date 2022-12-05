stacks = []
crates = []
tasks = []

with open('/Users/krauskopf/projects/adventofcode/2022/day5/input.txt') as f:
    for index, line in enumerate(f.readlines()):
        if(line.strip().startswith("[")):
            line = line.replace("\n", "")
            crates.append([line[i] for i in range(1,len(line),4)])
            continue
        if line.strip().startswith("1"):
            for _ in range(0, int(line.strip()[-1])):
                stacks.append([])
        if line.strip().startswith("move"):
            chars = line.strip().split(" ")
            tasks.append([int(char) for char in chars if char.isdigit()])

for line in crates:
    for index, char in enumerate(line):
        if char != " ":
            stacks[index].append(char)

input = []
for stack in stacks:
    input.append(stack[::-1])
    
# SOLVE 1
# for task in tasks:
#     print(task)
#     for _ in range(0,task[0]):
#         input[task[2]-1].append(input[task[1]-1].pop())

for task in tasks:
    print(task)
    buffer = []
    for _ in range(0,task[0]):
        buffer.append(input[task[1]-1].pop())
    buffer_reversed = buffer[::-1]
    for char in buffer_reversed:
        input[task[2]-1].append(char)

result = ""
for stack in input:
    result = result + stack.pop()

print(result)
