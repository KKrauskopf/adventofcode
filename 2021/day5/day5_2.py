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

def filter_lines(lines):
    for line in lines:
        x1 = int(line[0][0])
        x2 = int(line[1][0])
        y1 = int(line[0][1])
        y2 = int(line[1][1])
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 -y2)
    return [line for line in lines if x1 == x2 or y1 == y2 or x_diff == y_diff]


def solve2(lines):
    filtered_lines = filter_lines(lines)

    for line in filtered_lines:
        add_points(line)
    print(grid)
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

    if(run_x and not run_y):
        run_in_x_direction(x1, x2, y1)
    elif(run_y and not run_x):
        run_in_y_direction(x1, y1, y2)
    else:
        run_diagonally(x1, x2, y1, y2)

def run_in_y_direction(x1, y1, y2):
    if(y1 < y2):
        while y1 <= y2:
            update_grid(x1, y1)
            y1 += 1
    else:
        while y1 >= y2:
            update_grid(x1, y1)
            y1 -= 1

def run_in_x_direction(x1, x2, y1):
    if(x1 < x2):
        while x1 <= x2:
            update_grid(x1, y1)
            x1 += 1
    else:
        while x1 >= x2:
            update_grid(x1, y1)
            x1 -= 1

def run_diagonally(x1, x2, y1, y2):
    step_to_take = determine_direction(x1, x2, y1, y2)
    while x1 != x2 and y1 != y2:
        update_grid(x1, y1)
        x1 += step_to_take[0]
        y1 += step_to_take[1]
    # add the last point
    update_grid(x1, y1)

def determine_direction(x1, x2, y1, y2):
    x_diff_pos = x1 - x2 > 0
    y_diff_pos = y1- y2 > 0
    if(x_diff_pos and y_diff_pos):
        return [-1,-1]
    elif(not x_diff_pos and y_diff_pos):
        return [1,-1]
    elif(x_diff_pos and not y_diff_pos):
        return [-1,1]
    else:
        return [1,1]

def update_grid(x1, y1):
    key = build_key(x1, y1)
    if(key in grid):
        grid[key] = grid[key] +1
    else:
        grid[key] = 1

def build_key(x , y):
    return str(x) + "," + str(y)

print(solve2(lines))
