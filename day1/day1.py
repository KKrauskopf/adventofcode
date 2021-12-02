lines = []
slidingWindows = []

with open('/Users/krauskopf/projects/adventofcode/day1/input.txt') as f:
    for line in f.readlines():
        lines.append(int(line.strip()))

def build_sliding_windows(lines):
    for i in range(len(lines)-2):
        window = lines[i] + lines[i+1] + lines[i+2]
        slidingWindows.append(window)

def result(lines):
    counter = 0
    for i in range(len(lines)-1):
        # print("comparing {} to {}", lines[i], lines[i+1])
        if(lines[i] < lines[i+1]):
            counter += 1
    return counter

build_sliding_windows(lines)
hehe = result(slidingWindows)

print(slidingWindows.pop())
print(hehe)
