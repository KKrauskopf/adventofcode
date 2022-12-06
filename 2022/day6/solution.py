input = ""

with open('/Users/krauskopf/projects/adventofcode/2022/day5/input.txt') as f:
    for index, line in f.readlines():
        input = line

def solve1():
    chars = list(input)
    for i in range(3, len(chars)):
        check_range = set(chars[i],chars[i-1],chars[i-2],chars[i-3])
        print(len(check_range))

solve1()