input = ""

with open('/Users/krauskopf/projects/adventofcode/2022/day6/input.txt') as f:
    for line in f.readlines():
        input = line

def solve1():
    chars = list(input)
    for i in range(4, len(chars)):
        check_range = set([chars[i],chars[i-1],chars[i-2],chars[i-3]])
        if len(check_range) == 4:
            print(i+1)
            break

def solve2():
    chars = list(input)
    for i in range(14, len(chars)):
        check_range = set([chars[i],chars[i-1],chars[i-2],chars[i-3],chars[i-4],chars[i-5],chars[i-6],chars[i-7],chars[i-8],chars[i-9],chars[i-10],chars[i-11],chars[i-12],chars[i-13]])
        if len(check_range) == 14:
            print(i+1)
            break

solve2()