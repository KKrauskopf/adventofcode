grid = []

with open('/Users/krauskopf/projects/adventofcode/day11/input.txt') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = int(grid[i][j])

def solve1(grid):
    count = 100
    score = 0
    while count > 0:
        visited=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] <= 9): grid[i][j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] > 9 and [i,j] not in visited):
                    flash([i,j], grid, visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] > 9):
                    grid[i][j] = 0
        score += len(visited)
        count -= 1
    print(score)

def flash(squid, grid, visited):
    visited.append(squid)
    steps = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
    for step in steps:
        new_i, new_j = squid[0] + step[0], squid[1] + step[1]
        if(new_i <= len(grid) - 1 and new_i >= 0 and new_j <= len(grid[0]) - 1 and new_j >= 0):
            if(grid[new_i][new_j] <= 9):
                grid[new_i][new_j] += 1
            if(grid[new_i][new_j] > 9 and [new_i, new_j] not in visited):
                flash([new_i,new_j], grid, visited)

def solve2(grid):
    step = 0
    while True:
        visited=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] <= 9): grid[i][j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] > 9 and [i,j] not in visited):
                    flash([i,j], grid, visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] > 9):
                    grid[i][j] = 0
        zeros = sum([el.count(0) for el in grid])
        step += 1
        if(zeros == len(grid) * len(grid[0])):
            break
    print(step)



solve2(grid)