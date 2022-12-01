import time

lines = []

with open('/Users/krauskopf/projects/adventofcode/day9/input.txt') as f:
    for line in f.readlines():
        result = []
        new_line = list(line.strip())
        for char in new_line:
            result.append(int(char))
        lines.append(result)

def solve1(lines):
    score = 0
    low_points = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if(findLowPoint(lines, i, j)):
                score += lines[i][j] +1
                low_points.append([i,j])
    print(score)
    return low_points

def findLowPoint(lines, i, j):
    steps = [[1,0],[-1,0],[0,1],[0,-1]]
    isLowPoint = True
    for step in steps:
        new_x = i + step[0]
        new_y = j + step[1]
        if(new_y <= len(lines[0]) - 1 and new_y >= 0):
            if(new_x <= len(lines) - 1 and new_x >= 0):
                if(lines[new_x][new_y] <= lines[i][j]):
                    isLowPoint = False
                    break
    return isLowPoint

basins = []

def solve2(low_points):
    for point in low_points:
        basin = []
        basin.append(point)
        result = check_surroundings(point, basin)
        basins.append(result)
    len_list = [len(element) for element in basins]
    len_list.sort()
    print(len_list)
    score = len_list.pop() * len_list.pop() * len_list.pop()
    print(score)


def check_surroundings(point, basin):
    x, y = point[0], point[1]
    steps = [[1,0],[-1,0],[0,1],[0,-1]]
    for step in steps:
        new_x, new_y = x + step[0], y + step[1]
        if(new_y <= len(lines[0]) - 1 and new_y >= 0 and new_x <= len(lines) - 1 and new_x >= 0 and lines[new_x][new_y] != 9):
            if [new_x, new_y] not in basin:
                basin.append([new_x, new_y])
                check_surroundings([new_x, new_y], basin)
    return basin

solve2(solve1(lines))