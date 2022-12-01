
import time

lines = []

with open('/Users/krauskopf/projects/adventofcode/day8/input.txt') as f:
    for line in f.readlines():
        single_input = []
        parts = line.split("|")
        for part in parts:
            part = part.strip()
            single_input.append(part.split())
        lines.append(single_input)

def solve1(input):
    number_of_1_4_7_8 = 0
    for entry in input:
        output = entry[1]
        number_of_1_4_7_8 += sum([1 for number in output if len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7])
    print(number_of_1_4_7_8)

def solve2(input):
    ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = ("x","x","x","x","x","x","x","x","x","x")
    score = 0
    for entry in input:
        patterns, output = entry[0], entry[1]
        decode_map = {}
        candidates_5 = []
        candidates_6 = []
        for pattern in patterns:
            if len(pattern) == 2: ONE = pattern
            if len(pattern) == 3: SEVEN = pattern
            if len(pattern) == 4: FOUR = pattern
            if len(pattern) == 7: EIGHT = pattern
            if len(pattern) == 5: candidates_5.append(pattern)
            if len(pattern) == 6: candidates_6.append(pattern)

        for candidate in candidates_5:
            if(len(set(candidate).intersection(SEVEN)) == 3): THREE = candidate
            elif(len(set(candidate).intersection(FOUR)) == 3 and candidate != THREE): FIVE = candidate
            else: TWO = candidate

        for candidate in candidates_6:
            if(len(set(candidate).intersection(ONE)) == 1): SIX = candidate
            elif(len(set(candidate).intersection(FOUR)) == 4 and candidate != SIX): NINE = candidate
            else: ZERO = candidate

        for idx, el in enumerate([ZERO, ONE, TWO , THREE, FOUR, FIVE, SIX, SEVEN , EIGHT, NINE]):
            key = sorted(el)
            decode_map["".join(key)] = str(idx)

        encoded = ""
        for number in output:
            key = sorted(number)
            encoded += decode_map["".join(key)]
        score += int(encoded)
    print(score)



start = time.time()
solve2(lines)
end = time.time()
print("took ", round((end - start) * 1000,2), "ms")