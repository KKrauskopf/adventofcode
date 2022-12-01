draws = [72,86,73,66,37,76,19,40,77,42,48,62,46,3,95,17,97,41,10,14,83,90,12,23,81,98,11,57,13,69,28,63,5,78,79,58,54,67,60,34,39,84,94,29,20,0,24,38,43,51,64,18,27,52,47,74,59,22,85,65,80,2,99,70,33,91,53,93,9,82,8,50,7,56,30,36,89,71,21,49,31,88,26,96,16,1,75,87,6,61,4,68,32,25,55,44,15,45,92,35]

boards = []

with open('/Users/krauskopf/projects/adventofcode/day4/input.txt') as f:
    lines = []
    count = 1
    for line in f.readlines():
        if(count % 6 != 0):
            lines.append(line.strip())
        count +=1
    boardsCount = int(len(lines) / 5)
    for i in range (0,boardsCount):
        board = []
        for j in range(0,5):
            board.append(lines[(i*5)+j].split())
        boards.append(board)

def solve1(draws, boards):
    print(boards)
    index_of_board_that_won = -1
    last_draw = 0
    for draw in draws:
        draw = str(draw)
        index_of_board_that_won = checkForWinner(draw, boards)
        if(index_of_board_that_won != -1):
            last_draw = int(draw)
            break
    print(boards[index_of_board_that_won])
    score = calculateScore(boards[index_of_board_that_won], last_draw)
    return score

def checkForWinner(draw, boards):
    for id_board, board in enumerate(boards):
        # remove value
        for id_row, row in enumerate(board):
            for id_value, value in enumerate(row):
                if(value == draw):
                    board[id_row][id_value] = "X"
        if(checkHirozontally(board) or checkVertically(board)):
            return id_board
    return -1


def checkVertically(board):
    for i in range(0,5):
        column = [row[i] for row in board]
        if(checkRow(column)):
            return True
    return False

def checkHirozontally(board):
    for row in board:
        if(checkRow(row)):
            return True
    return False

def checkRow(row):
    return row.count("X") == 5


def calculateScore(board, last_draw):
    sum_of_remaining = 0
    for row in board:
        for value in row:
            if(value != "X"):
                print(value)
                sum_of_remaining += int(value)
    print(sum_of_remaining)
    return sum_of_remaining * last_draw

print(solve1(draws, boards))