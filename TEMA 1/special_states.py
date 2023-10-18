import random

def intialize(n, m, last_move): #n - linii, m - coloane
    state = []
    numbers = [i for i in range(n * m)]
    
    for i in range(n * m):
        x = random.randint(0, (len(numbers) - 1))
        y = numbers.pop(x)
        if y == 0:
            last_move[0] = i
        state += [y]

    while is_final_state(state):
        state = intialize(n, m)

    return state

def is_final_state(state) -> bool:
    for i in range(0, len(state) - 1):
        if state[i] > state[i + 1] and state[i + 1] != 0: #nu e in ordine crescatoare
            return False    
    return True