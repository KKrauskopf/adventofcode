import itertools as it

rucksacks = []
abc = "abcdefghijklmnopqrstuvwxyz"
letters = "0" + abc + abc.upper()

with open('/Users/krauskopf/projects/adventofcode/2022/day3/input.txt') as f:
    for line in f.readlines():
        rucksacks.append(line.strip())

def solve1(rucksacks):
    score = 0
    for rucksack in rucksacks:
        firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        firstset = set(firstpart)
        secondset = set(secondpart)
        common_member = firstset.intersection(secondset).pop()
        priority = letters.index(common_member)
        score += priority
    return score

def solve2(rucksacks):
    score = 0
    while len(rucksacks) > 0:
        first = set(rucksacks.pop())
        second = set(rucksacks.pop())
        third = set(rucksacks.pop())
        common_member = first.intersection(second).intersection(third).pop()
        priority = letters.index(common_member)
        score += priority
    return score

print(solve2(rucksacks))
