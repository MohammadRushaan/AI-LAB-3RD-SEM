cap_a = 7
cap_b = 4
GOAL = 5

def get_next_states(state):
    a, b = state
    moves = []

    if a < cap_a:
        moves.append((cap_a, b))
    
    if b < cap_b:
        moves.append((a, cap_b))
    
    if a > 0:
        moves.append((0, b))
    
    if b > 0:
        moves.append((a, 0))
    
    if a > 0 and b < cap_b:
        pour = min(a, cap_b - b)
        moves.append((a - pour, b + pour))
    
    if b > 0 and a < cap_a:
        pour = min(b, cap_a - a)
        moves.append((a + pour, b - pour))

    return moves

def solve_bfs():
    # queue holds (current_states, steps_taken)
    queue = [((0, 0), [(0, 0)])]
    visited = [(0, 0)]

    while len(queue) > 0:
        current, path = queue.pop(0)  

        if current[0] == GOAL or current[1] == GOAL:
            return path

        for next in get_next_states(current):
            if next not in visited:
                visited.append(next)
                queue.append((next, path + [next]))
                print(queue)

    return None

def solve_dfs():
    stack = [((0, 0), [(0, 0)])]
    visited = [(0, 0)]
    
    while len(stack) > 0:
        current, path = stack.pop()  

        if current[0] == GOAL or current[1] == GOAL:
            return path

        for next in get_next_states(current):
            if next not in visited:
                visited.append(next)
                stack.append((next, path + [next]))
                print(stack)

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