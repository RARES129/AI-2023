import time

# first_list = [8, 6, 7, 2, 5, 4, 0, 3, 1]

# first_list = [2, 5, 3, 1, 0, 6, 4, 7, 8]

# first_list = [2, 7, 5, 0, 8, 4, 3, 1, 6]


depth_limit = 4

goal_states = [
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [1, 2, 3, 4, 5, 6, 7, 0, 8],
    [1, 2, 3, 4, 5, 6, 0, 7, 8],
    [1, 2, 3, 4, 5, 0, 6, 7, 8],
    [1, 2, 3, 4, 0, 5, 6, 7, 8],
    [1, 2, 3, 0, 4, 5, 6, 7, 8],
    [1, 2, 0, 3, 4, 5, 6, 7, 8],
    [1, 0, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
]


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
    matrix = duplicate_matrix(current_state)
    index1, index2 = empty_cell(matrix)
    if index2 < len(matrix[0]) - 1:
        matrix[index1][index2], matrix[index1][index2 + 1] = (
            matrix[index1][index2 + 1],
            matrix[index1][index2],
        )
        return matrix
    return None


def manhattan_distance(current_state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != 0:
                x_goal, y_goal = divmod(goal_state.index(current_state[i][j]), 3)
                x_current, y_current = i, j
                x_distance = abs(x_goal - x_current)
                y_distance = abs(y_goal - y_current)
                distance += x_distance + y_distance
    return distance


def hamming_distance(current_state, goal_state):
    goal_state = [goal_state[i : i + 3] for i in range(0, len(goal_state), 3)]
    distance = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != goal_state[i][j]:
                distance += 1
    return distance


def chebyshev_distance(current_state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != 0:
                x_goal, y_goal = divmod(goal_state.index(current_state[i][j]), 3)
                x_current, y_current = i, j
                x_distance = abs(x_goal - x_current)
                y_distance = abs(y_goal - y_current)
                distance = max(distance, max(x_distance, y_distance))
    return distance


def best_distance(current_state, tipe):
    min_distance = float("inf")
    for goal_state in goal_states:
        if tipe == "HAMMING":
            distance = hamming_distance(current_state, goal_state)
        elif tipe == "MANHATTAN":
            distance = manhattan_distance(current_state, goal_state)
        elif tipe == "CHEBYSHEV":
            distance = chebyshev_distance(current_state, goal_state)
        if distance < min_distance:
            min_distance = distance
    return min_distance


def greedy(current_state, tipe):
    start_time = time.time()
    visited_states = set()
    count = 0
    queue = [(current_state, 0)]
    while queue:
        state = queue.pop(0)[0]
        if final(state):
            end_time = time.time()
            total_time = end_time - start_time
            print("\n", tipe, ": ", state, sep="")
            print("Moves: ", count)
            print("Time: ", total_time)
            return state, count, total_time
        visited_states.add(str(state))
        for move in [up, down, left, right]:
            new_state = move(state)
            if new_state is not None and str(new_state) not in visited_states:
                queue.append((new_state, best_distance(new_state, tipe)))
                count += 1
        queue.sort(key=lambda x: x[1])
    end_time = time.time()
    total_time = end_time - start_time
    print(tipe, "No solution found :(")
    print("Moves: ", count)
    print("Time: ", total_time)
    return None


def iddfs(current_state):
    start_time = time.time()
    count = 0
    for depth in range(1, depth_limit + 1):
        visited_states = set()
        stack = [(current_state, 0)]
        while stack:
            state, current_depth = stack.pop()
            if final(state):
                end_time = time.time()
                total_time = end_time - start_time
                print("\nIDDFS: ", state, sep="")
                print("Moves: ", count)
                print("Time: ", total_time)
                return state, count, total_time
            if current_depth == depth:
                continue
            visited_states.add(str(state))
            for move in [up, down, left, right]:
                new_state = move(state)
                if new_state is not None and str(new_state) not in visited_states:
                    stack.append((new_state, current_depth + 1))
                    count += 1

    end_time = time.time()
    total_time = end_time - start_time
    print("\nIDDFS: No solution found :(", sep="")
    print("Moves: ", count)
    print("Time: ", total_time)
    return None


def main():
    first_state = initialize(first_list)
    iddfs(first_state)
    greedy(first_state, "HAMMING")
    greedy(first_state, "MANHATTAN")
    greedy(first_state, "CHEBYSHEV")


main()
