def get_user_input():
    val=0
    while (val<=1):
        val = int(input("Enter the board size n (n > 1): "))
        if val > 1:
            return val
        print("Please enter an integer strictly greater than 1.")

def print_board(board):
    # Print a board cleanly
    for row in board:
        print("  " + " ".join(row))
    print()


def solve_n_queens(n):
    board = []
    for i in range(n):
        row = ["."] * n
        board.append(row)
    solutions = []

    cols = set()
    diag1 = set()  # (r - c)
    diag2 = set()  # (r + c)
    step = [0]

    def backtrack(r):
        # Base case: reached past the last row -> valid solution found
        if r == n:
            solutions.append([" ".join(row) for row in board])
            print(f"*** FOUND SOLUTION #{len(solutions)} ***")
            print_board(board)
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            # Place queen (state modification)
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            step[0] += 1
            print(f"[Step {step[0]}] Place Queen at ({r}, {c}):")
            print_board(board)

            # Recurse to next row
            backtrack(r + 1)

            # Backtrack (revert state)
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
            step[0] += 1
            print(f"[Step {step[0]}] Backtrack from ({r}, {c}):")
            print_board(board)

    backtrack(0)
    return solutions


def main():
    n = get_user_input()

    print("")
    print(f"Solving {n}-Queens Problem (Intermediate Steps)")
    print("")

    solutions = solve_n_queens(n)

    print("")
    print(f"Total valid configurations found: {len(solutions)}")
    if len(solutions) == 0:
        print(f"Note: No feasible solution exists for n = {n}.")
    print("")

main()