# depth = 4
# first_list = [2, 5, 3, 1, 0, 6, 4, 7, 8]

# depth = 3
# first_list = [1, 0, 2, 4, 5, 3, 7, 8, 6]

# depth = 2
# first_list = [1, 2, 0, 4, 5, 3, 7, 8, 6]

# depth = 1
first_list = [1, 2, 3, 4, 5, 0, 7, 8, 6]

# depth = 0
# first_list = [1, 2, 3, 4, 0, 5, 6, 7, 8]

depth_limit = 10


def duplicate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    duplicated_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for index1 in range(rows):
        for index2 in range(cols):
            duplicated_matrix[index1][index2] = matrix[index1][index2]

    return duplicated_matrix


def initialize(first_list):
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for index1 in range(0, len(first_list)):
        matrix[index1 // 3][index1 % 3] = first_list[index1]
    return matrix


def final(current_state):
    final_list = []
    sorted_list = []
    for index1 in range(0, len(current_state)):
        for index2 in range(0, len(current_state[0])):
            final_list.append(current_state[index1][index2])
    final_list.remove(0)
    sorted_list = sorted(final_list)
    if sorted_list == final_list:
        return True
    return False


def equal(state, other):
    if other is None or state is None:
        return False

    for index1 in range(0, len(state)):
        for index2 in range(0, len(state[0])):
            if state[index1][index2] != other[index1][index2]:
                return False
    return True


def empty_cell(current_state):
    for index1 in range(0, len(current_state)):
        for index2 in range(0, len(current_state[0])):
            if current_state[index1][index2] == 0:
                return index1, index2
    return False


def up(current_state):
    print("Move up")
    index1, index2 = empty_cell(current_state)
    matrix = duplicate_matrix(current_state)
    if index1 > 0:
        matrix[index1][index2], matrix[index1 - 1][index2] = (
            matrix[index1 - 1][index2],
            matrix[index1][index2],
        )
        return matrix
    return None


def down(current_state):
    print("Move down")
    matrix = duplicate_matrix(current_state)
    index1, index2 = empty_cell(matrix)
    if index1 < len(matrix) - 1:
        matrix[index1][index2], matrix[index1 + 1][index2] = (
            matrix[index1 + 1][index2],
            matrix[index1][index2],
        )
        return matrix
    return None


def left(current_state):
    print("Move left")
    matrix = duplicate_matrix(current_state)
    index1, index2 = empty_cell(matrix)
    if index2 > 0:
        matrix[index1][index2], matrix[index1][index2 - 1] = (
            matrix[index1][index2 - 1],
            matrix[index1][index2],
        )
        return matrix
    return None


def right(current_state):
    print("Move right")
    matrix = duplicate_matrix(current_state)
    index1, index2 = empty_cell(matrix)
    if index2 < len(matrix[0]) - 1:
        matrix[index1][index2], matrix[index1][index2 + 1] = (
            matrix[index1][index2 + 1],
            matrix[index1][index2],
        )
        return matrix
    return None


def algorithm_iddfs(state, depth, maximum_depth, last_state):
    if state is None:
        return None
    if final(state):
        print("SOLVED AT DEPTH: " + str(depth))
        print("FINAL STATE IS: " + str(list(state)))
        return True
    print("At depth: -> " + str(depth))
    if depth == maximum_depth:
        return None
    if not equal(state, up(state)) and not equal(last_state, up(state)):
        if algorithm_iddfs(up(state), depth + 1, maximum_depth, state):
            return True
    if not equal(state, left(state)) and not equal(last_state, left(state)):
        if algorithm_iddfs(left(state), depth + 1, maximum_depth, state):
            return True
    if not equal(state, right(state)) and not equal(last_state, right(state)):
        if algorithm_iddfs(right(state), depth + 1, maximum_depth, state):
            return True
    if not equal(state, down(state)) and not equal(last_state, down(state)):
        if algorithm_iddfs(down(state), depth + 1, maximum_depth, state):
            return True


def main():
    first_state = initialize(first_list)
    for index1 in range(0, depth_limit):
        if algorithm_iddfs(first_state, 0, index1, None):
            break


main()
