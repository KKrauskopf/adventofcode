lines = []

with open('/Users/krauskopf/projects/adventofcode/day10/input.txt') as f:
    for line in f.readlines():
        lines.append(list(line.strip()))

opening_chars= ["(", "[", "<", "{"]

score_map = {}
score_map[")"] = 3
score_map["]"] = 57
score_map["}"] = 1197
score_map[">"] = 25137
score_map[""] = 0

def solve1(lines):
    score = 0
    for line in lines:
        stack = []
        broken_char = ""
        for char in line:
            if(len(stack) == 0):
                stack.append(char)
                continue
            if(char in opening_chars):
                stack.append(char)
            else:
                last = stack[-1]
                if(last == "(" and char == ")" or last == "[" and char == "]" or last == "{" and char == "}" or last == "<" and char == ">"):
                    stack.pop()
                else:
                    broken_char = char
                    break
        score += score_map[broken_char]
    print(score)

score_map2 = {}
score_map2["("] = 1
score_map2["["] = 2
score_map2["{"] = 3
score_map2["<"] = 4

def solve2(lines):
    scores = []
    for line in lines:
        stack = []
        broken = False
        for char in line:
            if(len(stack) == 0):
                stack.append(char)
                continue
            if(char in opening_chars):
                stack.append(char)
            else:
                last = stack[-1]
                if(last == "(" and char == ")" or last == "[" and char == "]" or last == "{" and char == "}" or last == "<" and char == ">"):
                    stack.pop()
                else:
                    broken = True
        if(not broken):
            single_score = 0
            stack.reverse()
            for el in stack:
                single_score = single_score * 5
                single_score += score_map2[el]
            scores.append(single_score)
    scores.sort()
    while(len(scores) > 1):
        scores.pop()
        scores.pop(0)
    print(scores)

solve2(lines)
