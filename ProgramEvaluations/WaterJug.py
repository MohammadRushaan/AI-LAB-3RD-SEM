CAP_A = 7
CAP_B = 4
GOAL = 5

def get_next_states(state):
    a, b = state
    moves = []

    # Fill Jug A
    if a < CAP_A:
        moves.append((CAP_A, b))

    # Fill Jug B
    if b < CAP_B:
        moves.append((a, CAP_B))

    # Empty Jug A
    if a > 0:
        moves.append((0, b))

    # Empty Jug B
    if b > 0:
        moves.append((a, 0))

    # Pour Jug A to Jug B
    if a > 0 and b < CAP_B:
        pour = min(a, CAP_B - b)
        moves.append((a - pour, b + pour))

    # Pour Jug B to Jug A
    if b > 0 and a < CAP_A:
        pour = min(b, CAP_A - a)
        moves.append((a + pour, b - pour))

    return moves

def solve_bfs():
    # queue holds (current_state, list_of_steps_taken)
    queue = [((0, 0), [(0, 0)])]
    visited = [(0, 0)]

    while len(queue) > 0:
        current, path = queue.pop(0)  

        if current[0] == GOAL or current[1] == GOAL:
            return path

        for nxt in get_next_states(current):
            if nxt not in visited:
                visited.append(nxt)
                queue.append((nxt, path + [nxt]))
                #print(queue)

    return None

def solve_dfs():
    stack = [((0, 0), [(0, 0)])]
    visited = [(0, 0)]
    
    while len(stack) > 0:
        current, path = stack.pop()  

        if current[0] == GOAL or current[1] == GOAL:
            return path

        for nxt in get_next_states(current):
            if nxt not in visited:
                visited.append(nxt)
                stack.append((nxt, path + [nxt]))
                #print(stack)

    return None

bfs_path = solve_bfs()
dfs_path = solve_dfs()

def show_result(name, path):
    print(f"\n--- {name} ---")
    for i in range(len(path)):
        print("Step", i, ": Jug A =", path[i][0], "L, Jug B =", path[i][1], "L")
    print("Total Operations:", len(path) - 1)

show_result("BFS Solution (Shortest)", bfs_path)
show_result("DFS Solution", dfs_path)