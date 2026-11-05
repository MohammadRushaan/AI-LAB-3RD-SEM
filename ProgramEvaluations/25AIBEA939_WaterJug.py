"""
The Two Necessary & Sufficient Conditions:
A. target volume T can be measured if and only if
    T is less than the maximum vessel capacity

B. Divisibility by Greatest Common Divisor (GCD):
    target must be an exact multiple of the greatest common divisor of A and B
"""
import sys

cap_a=0
cap_b=0
GOAL=0

def condition(a,b,t):
    while b != 0:
        a, b = b, a % b
    abs(a)

    if t>a and t>b:
        state= True

    if t%a==0:
        state = False
    else:
        state = True

    if state == True:
        print("target precondition failed, no possible solution for given task")
        sys.exit()

def user_input():
    global cap_a, cap_b, GOAL
    cap_a = int(input("Enter capacity of Jug A: "))
    cap_b = int(input("Enter capacity of Jug B: "))
    GOAL = int(input("Enter target capacity: "))

    condition(cap_a,cap_b,GOAL)
    
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

def show_result(name, path):
    print(f"\n--- {name} ---")
    for i in range(len(path)):
        print("Step", i, ": Jug A =", path[i][0], "L, Jug B =", path[i][1], "L")
    print("Total Operations:", len(path) - 1)

def main():
    user_input()

    bfs_path = solve_bfs()
    dfs_path = solve_dfs()

    show_result("BFS Solution (Shortest)", bfs_path)
    show_result("DFS Solution", dfs_path)

main()