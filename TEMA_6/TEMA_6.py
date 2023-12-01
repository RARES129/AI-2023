import random

GRID_SIZE = (7, 10)
START_STATE = (3, 0)
GOAL_STATE = (3, 7)
WIND_STRENGTH = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
ACTIONS = ['up', 'down', 'left', 'right']
EPISODES = 1000
ALPHA = 0.1  
GAMMA = 0.9 
EPSILON = 0.1  


Q = {}
for i in range(GRID_SIZE[0]):
    for j in range(GRID_SIZE[1]):
        Q[(i, j)] = {a: 0 for a in ACTIONS}

def get_next_state(current_state, action):
    row, col = current_state
    wind_effect = WIND_STRENGTH[col]
    
    if action == 'up':
        row -= (1 + wind_effect)
    elif action == 'down':
        row += (1 + wind_effect)
    elif action == 'left':
        col -= 1
    elif action == 'right':
        col += 1
    
    row = max(0, min(row, GRID_SIZE[0] - 1))
    col = max(0, min(col, GRID_SIZE[1] - 1))
    
    return (row, col)

def q_learning():
    current_state = START_STATE

    for episode in range(EPISODES):
        while current_state != GOAL_STATE:
            if random.uniform(0, 1) < EPSILON:
                action = random.choice(ACTIONS)
            else:
                action = max(Q[current_state], key=Q[current_state].get)

            next_state = get_next_state(current_state, action)
            
            Q[current_state][action] += ALPHA * (
                -1 + GAMMA * max(Q[next_state].values()) - Q[current_state][action]
            )

            current_state = next_state

    return Q

def show_policy(Q):
    policy = {}
    for state in Q:
        policy[state] = max(Q[state], key=Q[state].get)
    return policy

def main():
    Q = q_learning()
    policy = show_policy(Q)
    print("Q-table:")
    for state, values in Q.items():
        print(f"State: {state}, Q-values: {values}")
    print("\nPolicy:")
    for state, action in policy.items():
        print(f"State: {state}, Action: {action}")

main()
