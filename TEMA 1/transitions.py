def validate_transition(state, cell, last_move) -> bool:
    """ 
        - verific daca pot sa interchimb celula goala cu valoarea(=pozitia) celui de-al doilea parametru
        - last_move ne asigura ca nu vom forma bucla mutand aceeasi piesa
    """

    if cell == last_move[0]:
        return False

    for i in [-3, -1, 1, 3]:
        if (cell + i) >= 0 and (cell + i) <= 8:
            if state[cell + i] == 0:
                return True

    return False

def make_transiton(state, cell, last_move):
    new_state = []

    if not validate_transition(state, cell, last_move):
        return None
    
    zero = 0
    for i in state:
        if state[i] == 0:
            zero = i
            break

    last_move[0] = cell
    aux = state[cell]

    new_state = state[:cell]
    new_state += [0]
    new_state += state[cell + 1: zero]
    new_state += [aux]
    new_state += state[zero + 1:]

    return new_state