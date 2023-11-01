import copy


def get_empty_cells(board):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 or board[i][j] == -1:
                empty_cells.append((i, j))
    return empty_cells


def get_possible_values(board, row, col):
    values = set(range(1, 10))
    if board[row][col] == -1:
        values = [2, 4, 6, 8]
    for j in range(9):
        if board[row][j] in values:
            values.remove(board[row][j])
    for i in range(9):
        if board[i][col] in values:
            values.remove(board[i][col])
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] in values:
                values.remove(board[i][j])
    return list(values)


def forward_checking(board, empty_cells, domain):
    new_domain = copy.deepcopy(domain)
    for cell in empty_cells:
        row, col = cell
        values = new_domain[(row, col)]
        for j in range(9):
            if board[row][j] in values:
                values.remove(board[row][j])
        for i in range(9):
            if board[i][col] in values:
                values.remove(board[i][col])
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] in values:
                    values.remove(board[i][j])
        new_domain[(row, col)] = values
    return new_domain


def mrv(empty_cells, domain):
    min_cell = None
    min_values = float("inf")
    for cell in empty_cells:
        values = domain[cell]
        if len(values) < min_values:
            min_cell = cell
            min_values = len(values)
    return min_cell


def solve_sudoku(board, empty_cells, domain):
    if not empty_cells:
        return board
    cell = mrv(empty_cells, domain)
    values = domain[cell]
    for value in values:
        new_board = copy.deepcopy(board)
        new_board[cell[0]][cell[1]] = value
        new_empty_cells = empty_cells.copy()
        new_empty_cells.remove(cell)
        new_domain = forward_checking(new_board, new_empty_cells, domain)
        if all(len(new_domain[cell]) > 0 for cell in new_empty_cells):
            result = solve_sudoku(new_board, new_empty_cells, new_domain)
            if result:
                return result
    return None


def main():
    board = [
        [8, 4, 0, 0, 5, 0, -1, 0, 0],
        [3, 0, 0, 6, 0, 8, 0, 4, 0],
        [0, 0, -1, 4, 0, 9, 0, 0, -1],
        [0, 2, 3, 0, -1, 0, 9, 8, 0],
        [1, 0, 0, -1, 0, -1, 0, 0, 4],
        [0, 9, 8, 0, -1, 0, 1, 6, 0],
        [-1, 0, 0, 5, 0, 3, -1, 0, 0],
        [0, 3, 0, 1, 0, 6, 0, 0, 7],
        [0, 0, -1, 0, 2, 0, 0, 1, 3],
    ]
    empty_cells = get_empty_cells(board)
    domain = {}
    for cell in empty_cells:
        domain[cell] = get_possible_values(board, cell[0], cell[1])

    board_final = solve_sudoku(board, empty_cells, domain)
    if board_final:
        for row in board_final:
            print(row)
    else:
        print("Nu exista solutie")


main()
