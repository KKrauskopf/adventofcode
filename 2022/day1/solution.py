elves = []
lines = []

with open('/Users/krauskopf/projects/adventofcode/2022/day1/input.txt') as f:
    for line in f.readlines():
        if line in ['\n', '\r\n']:
            elves.append(list(lines))
            lines.clear()
        else:
            lines.append(int(line.strip()))
    elves.append(list(lines))

calories = []

for elve in elves:
    calories.append(sum(elve))

# solution 1
# print(max(calories))

# solution 2
calories.sort()
print(sum(calories[len(calories)-3:]))
# for i in range (0,2):
