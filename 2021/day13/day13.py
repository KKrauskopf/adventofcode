grid = []
instructions = []

with open('/Users/krauskopf/projects/adventofcode/day13/input.txt') as f:
    points = []
    for line in f.readlines():
        if len(line) <= 1: continue
        if(line.startswith("fold")):
            instruction = line.strip().split()[2]
            dir, value = instruction.split("=")
            instructions.append([dir,int(value)])
        else:
            x,y = line.strip().split(",")
            points.append([int(x),int(y)])
    max_x = max([point[0] for point in points])+1
    max_y = max([point[1] for point in points])+1
    line = ["."] * (max_x)
    for j in range(0,max_y):
        grid.append(list(line))
    for point in points:
        grid[point[1]][point[0]] = "#"

def solve1(grid):
    for fold in instructions:
        if(fold[0] == "y"): grid = fold_up(fold[1], grid)
        else: grid = fold_left(fold[1], grid)
        break
    score = 0
    for line in grid:
        score += line.count("#")
    print(score)

def solve2(grid):
    for fold in instructions:
        if(fold[0] == "y"): grid = fold_up(fold[1], grid)
        else: grid = fold_left(fold[1], grid)
    score = 0
    for line in grid:
        score += line.count("#")
        print(line)

def fold_up(axis, grid):
    for i in range(axis,len(grid)):
        for idx, point in enumerate(grid[i]):
            if(point == "#"):
                new_y = axis-abs(axis-i)
                grid[new_y][idx] = point
    return grid[:axis+1]

def fold_left(axis, grid):
    for i in range(0,len(grid)):
        for idx, point in enumerate(grid[i]):
            if(idx >= axis and point == "#"):
                new_x = axis-abs(axis-idx)
                grid[i][new_x] = point
    new_grid = []
    for line in grid:
        new_grid.append(line[:axis])
    return new_grid




solve1(grid)
solve2(grid)