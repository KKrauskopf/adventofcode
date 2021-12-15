from collections import defaultdict

start= list("PPFCHPFNCKOKOSBVCFPP")

mappings = defaultdict(list)

with open('/Users/krauskopf/projects/adventofcode/day14/input.txt') as f:
    for line in f.readlines():
        inp, out = line.strip().split("->")
        split_input = list(inp)
        out = out.strip()
        mappings[inp.strip()] = [split_input[0]+out, out + split_input[1]]

def solve2(start):
    pair_counts = defaultdict(int)
    letter_counts = defaultdict(int)
    for i in range(0,len(start)-1):
        pair_counts[start[i] + start[i+1]] += 1
    for char in start:
        letter_counts[char] += 1
    for i in range(0,40):
        new_pair_counts = defaultdict(int)
        for key, value in pair_counts.items():
            child1, child2 = list(mappings[key])
            new_pair_counts[child1] += value
            new_pair_counts[child2] += value
            letter_counts[child1[1:]] += value
        pair_counts = new_pair_counts

    #letter_values = [value/2 if value %2 == 0 else (value-1)/2 for _ ,value in letters.items()]
    letter_values = [value for value in letter_counts.values()]
    maxv = max(letter_values)
    minv = min(letter_values)
    print(maxv - minv)

print(solve2(start))