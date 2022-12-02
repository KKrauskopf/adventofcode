combinations = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

mapper = {
    "A X": "A Z", "A Y": "A X", "A Z": "A Y",
    "B X": "B X", "B Y": "B Y", "B Z": "B Z",
    "C X": "C Y", "C Y": "C Z", "C Z": "C X"
}

games = []

with open('/Users/krauskopf/projects/adventofcode/2022/day2/input.txt') as f:
    for line in f.readlines():
        games.append(mapper.get(line.strip()))

score = 0

print(games)

for game in games:
    score += combinations.get(game)

print(score)



# combinations = {
#     "A X": 4, "A Y": 8, "A Z": 3,
#     "B X": 1, "B Y": 5, "B Z": 9,
#     "C X": 7, "C Y": 2, "C Z": 6
# }

# games = []

# with open('/Users/krauskopf/projects/adventofcode/2022/day2/input.txt') as f:
#     for line in f.readlines():
#         games.append(line.strip())

# score = 0

# print(games)

# for game in games:
#     score += combinations.get(game)

# print(score)