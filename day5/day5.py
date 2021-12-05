lines = []
grid = {}

with open('/Users/krauskopf/projects/adventofcode/day5/input.txt') as f:
    for line in f.readlines():
        parts = line.split("->")
        result = []
        for part in parts:
            part = part.strip()
            point = part.split(",")
            result.append(point)
        lines.append(result)

def solve1(lines):
    filtered_lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

    for line in filtered_lines:
        add_points(line)

    return find_score(grid)

def find_score(grid):
    counter = 0
    for key, value in grid.items():
        if value > 1:
            counter += 1
    return counter

def add_points(line):
    x1 = int(line[0][0])
    x2 = int(line[1][0])
    y1 = int(line[0][1])
    y2 = int(line[1][1])

    run_x = (x1 - x2) != 0
    run_y = (y1 - y2) != 0

    if(run_x):
        if(x1 < x2):
            while x1 <= x2:
                update_grid(x1, y1)
                x1 += 1
        else:
            while x1 >= x2:
                update_grid(x1, y1)
                x1 -= 1

    if(run_y):
        if(y1 < y2):
            while y1 <= y2:
                update_grid(x1, y1)
                y1 += 1
        else:
            while y1 >= y2:
                update_grid(x1, y1)
                y1 -= 1

def build_key(x , y):
    return str(x) + "," + str(y)

def update_grid(x1, y1):
    key = build_key(x1, y1)
    if(key in grid):
        grid[key] = grid[key] +1
    else:
        grid[key] = 1

print(solve1(lines))
