from math import inf as infinity

remain_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ai_values = []
human_values = []
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
# THE BOARD
"""
2 7 6
9 5 1
4 3 8
"""


def value(x, y):
    if x == 0 and y == 0:
        return 2
    elif x == 0 and y == 1:
        return 7
    elif x == 0 and y == 2:
        return 6
    elif x == 1 and y == 0:
        return 9
    elif x == 1 and y == 1:
        return 5
    elif x == 1 and y == 2:
        return 1
    elif x == 2 and y == 0:
        return 4
    elif x == 2 and y == 1:
        return 3
    elif x == 2 and y == 2:
        return 8


def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    return best


def render():
    print("\nRemain values: ", remain_values)
    print("AI values: ", ai_values)
    print("Human values: ", human_values)


def ai_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    print("\n------------------------------------------")
    print("COMPUTER TURN")
    move = minimax(board, depth, COMP)
    x, y = move[0], move[1]
    set_move(x, y, COMP)
    print("Computer choice: ", value(x, y))
    ai_values.append(value(x, y))
    remain_values.remove(value(x, y))


def human_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    move = -1
    moves = {
        2: [0, 0],
        7: [0, 1],
        6: [0, 2],
        9: [1, 0],
        5: [1, 1],
        1: [1, 2],
        4: [2, 0],
        3: [2, 1],
        8: [2, 2],
    }
    print("\n------------------------------------------")
    print("HUMAN TURN")
    render()
    while move < 1 or move > 9:
        move = int(input("Use numpad (1..9): "))
        if move < 10 and move > 0:
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)
            if not can_move:
                print("Bad move")
                move = -1
        else:
            print("Bad choice")
    human_values.append(value(coord[0], coord[1]))
    remain_values.remove(move)


def main():
    while len(empty_cells(board)) > 0 and not game_over(board):
        human_turn()
        ai_turn()
    if wins(board, HUMAN):
        render()
        print("YOU WIN!")
    elif wins(board, COMP):
        render()
        print("YOU LOSE!")
    else:
        render()
        print("DRAW!")
    exit()


main()
