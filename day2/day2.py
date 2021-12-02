lines = []
with open('/Users/krauskopf/projects/adventofcode/day2/input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

def calculate_position(lines):
    aim = 0
    depth = 0
    horizontal = 0
    for line in lines:
        splits = line.split()
        direction = splits[0]
        amount = int(splits[1])
        if(direction == "forward"):
            horizontal += amount
            depth += amount * aim
        if(direction == "down"):
            aim += amount
        if(direction == "up"):
            aim -= amount
    print(depth, horizontal)
    return depth * horizontal

print(calculate_position(lines))
