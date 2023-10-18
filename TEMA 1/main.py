import special_states
import transitions


def main():
    state = [8, 6, 7, 2, 5, 4, 0, 3, 1]  # intial state
    # state = [1, 2, 3, 4, 0, 5, 6, 7, 8] #final state
    # state = [1, 2, 3, 4, 0, 6, 7, 5, 8] #intermediate state
    last_move = [0]

    # state = special_states.intialize(3, 3, last_move)
    # print(last_move[0])
    # print(state)

    # new_state = transitions.make_transiton(state, 3, [0])
    # print(new_state)


main()
