start= list("PPFCHPFNCKOKOSBVCFPP")

mappings = {}

with open('/Users/krauskopf/projects/adventofcode/day14/input.txt') as f:
    for line in f.readlines():
        inp, out = line.strip().split("->")
        mappings[inp.strip()] = out.strip()

def solve1(start):
    result = start
    for i in range(0,40):
        print(i)
        result = expand_list(result)
    print(most_common(result) - least_common(result))

def most_common(list):
    return list.count(max(set(list), key=list.count))

def least_common(list):
    return list.count(min(set(list), key=list.count))

def expand_list(start):
    new_list = [None] * (len(start*2)-1)
    for idx, char in enumerate(start):
        new_list[idx*2] = char
    for i in range(1,len(new_list),2):
        new_list[i] = mappings[new_list[i-1] + new_list[i+1]]
    return new_list

print(solve1(start))