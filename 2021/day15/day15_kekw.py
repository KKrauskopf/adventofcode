grid = []

with open('/Users/krauskopf/projects/adventofcode/day15/input.txt') as f:
    for line in f.readlines():
        grid.append(list(map(int, list(line.strip()))))


risk_levels = []

def solve1():
    visited = []
    risk_level = - grid[0][0]
    visited = findPath(visited, risk_level, 0,0)
    print(risk_levels)

def findPath(visited, risk_level, row, col):
    risk_level += grid[row][col]
    visited.append([row,col])
    if(len(risk_levels) > 0):
        if(risk_level >= min(risk_levels)):
            return
    if(row == len(grid)-1 and col == len(grid[0])-1):
        risk_levels.append(risk_level)
        if(len(risk_levels) > 1):
            risk_levels.pop(0)
        #print(visited)
        return
    steps = [[1,0],[-1,0],[0,1],[0,-1]] # no diagonals
    for step in steps:
        new_row, new_col = row + step[0], col + step[1]
        if(check_bounds(new_row, new_col) and [new_row, new_col] not in visited):
            findPath(visited.copy(), risk_level, new_row, new_col)

def check_bounds(row, col):
    return row >= 0 and row <= len(grid)-1 and col >= 0 and col <= len(grid[0]) -1

solve1()