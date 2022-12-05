
input_int = []
input_str = []

with open('/Users/krauskopf/projects/adventofcode/2022/day4/input.txt') as f:
    for line in f.readlines():
        section1, section2 = line.strip().split(",")
        pair1, pair2 = list(section1.split("-")), list(section2.split("-"))
        pair3, pair4 = [int(i) for i in section1.split("-")], [int(j) for j in section2.split("-")]
        input_str.append([pair1,pair2])
        input_int.append([pair3,pair4])

def solve1_str(input):
    overlaps = []
    for pair in input:
        section1, section2 = pair[0], pair[1]
        substring1 = "".join([str(i) for i in range(int(section1[0]), int(section1[1])+1)])
        substring2 = "".join([str(i) for i in range(int(section2[0]), int(section2[1])+1)])
        print(substring1)
        print(substring2)
        if substring1 in substring2 or substring2 in substring1:
            overlaps.append(pair)
    return overlaps

def solve1_int(input):
    overlaps = []
    for pair in input:
        x1,x2,y1,y2, = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
        if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
            overlaps.append([[str(x1),str(x2)],[str(y1),str(y2)]])
    return overlaps

def solve2_int(input):
    overlaps = []
    for pair in input:
        x1,x2,y1,y2, = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
        if (x1 >= y1 and x1 <= y2) or (x2 <= y2 and x2 >= y1) or (y1 >= x1 and y1 <= x2) or (y2 <= x2 and y2 >= x1):
            overlaps.append([[str(x1),str(x2)],[str(y1),str(y2)]])
    return overlaps

print(len(solve2_int(input_int)))
