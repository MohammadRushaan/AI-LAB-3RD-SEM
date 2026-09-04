## The problem:

The N-Queens Problem asks how to place $N$ non-attacking queens on an $N \times N$ chessboard such that no two queens threaten each other. Under standard chess rules, a queen can attack any square along its row, column, or either diagonal.

## Core Concept & Mathematical Constraints:
To place $N$ mutually safe queens on an $N \times N$ board:
1. Row & Column Exclusivity: Exactly one queen must occupy each row and each column. We can place queens one row at a time (from row $0$ to $N-1$) and search for an available column.
2. Diagonal Exclusivity: For any square at $(r, c)$:
    Major Diagonal ($\backslash$): The difference between row and column indices is invariant: $r - c = \text{constant}$.
    Minor Diagonal ($/$): The sum of row and column indices is invariant: $r + c = \text{constant}$.

## Key Concepts & Algorithmic Mechanics:

* State Space Tree: The problem generates a tree where the root is an empty board, each level $k$ represents choices for row $k$, and leaves are candidate configurations.
* Backtracking: Instead of generating all $\binom{N^2}{N}$ placements or $N^N$ row-column permutations, backtracking constructs candidate solutions step by step. If placing a queen violates a constraint, the algorithm prunes the branch immediately, reverts the move, and retreats to try the next column in the previous row.

# N-Queens Problem: Comprehensive Reference & Implementation Guide

---

## 1. Data Structures & State Modifications

| Data Structure | Role | Modifications During Execution |
| :--- | :--- | :--- |
| **`board`** *(2D List)* | Represents the $N \times N$ physical grid (`'Q'` or `'.'`). | **Set:** `board[r][c] = 'Q'` on placement.<br>**Reset:** `board[r][c] = '.'` on backtrack. |
| **`cols`** *(Hash Set / Array)* | Tracks columns currently under attack. | `cols.add(c)` on placement;<br>`cols.remove(c)` on backtrack. |
| **`diag1`** *(Hash Set / Array)* | Tracks occupied major diagonals ($r - c$). | `diag1.add(r - c)` on placement;<br>`diag1.remove(r - c)` on backtrack. |
| **`diag2`** *(Hash Set / Array)* | Tracks occupied minor diagonals ($r + c$). | `diag2.add(r + c)` on placement;<br>`diag2.remove(r + c)` on backtrack. |
| **Call Stack** *(Implicit)* | Stores recursive execution frames. | Pushes the next frame for row $r + 1$; pops back to row $r$ when a path is exhausted. |

> Using lookup sets allows safety validation in $\mathcal{O}(1)$ time instead of traversing diagonals across the grid in $\mathcal{O}(N)$ time.

---

## 2. Program Execution Flow & Setup

Execution begins at the entry point block:

```python
if __name__ == "__main__":
    main()
```

This ensures `main()` executes only when the script runs directly, rather than when imported as a module.

---

## 3. Function-by-Function Breakdown

### `get_user_input()`
* **Purpose:** Safely fetches and validates the integer board size from standard input.
* **Mechanism:**
  * Uses an infinite `while True` loop to repeatedly prompt until valid data is entered.
  * Encapsulates `input()` inside a `try...except ValueError` block to handle non-numeric inputs (e.g., entering `"abc"` or `3.14`).
  * Enforces the constraint $n > 1$ before returning $n$.

### `print_board(board)`
* **Purpose:** Renders the 2D grid in human-readable board format.
* **Mechanism:**
  * Iterates over each row list in `board`.
  * Joins elements with spaces (`" ".join(row)`) so that `['.', 'Q', '.']` outputs cleanly as `. Q .`.

### `main()`
* **Purpose:** Orchestrates user input, solver execution, and final reporting.
* **Mechanism:**
  * Calls `get_user_input()` to obtain $n$.
  * Calls `solve_n_queens(n)`, receiving a list containing all successful configurations.
  * Prints summary boundaries, the total solution count (`len(solutions)`), and an explicit note for cases like $n = 2$ or $n = 3$ where no valid placement exists.

---

## 4. Deep Dive: `solve_n_queens(n)` & Internal Recursion

This function sets up the state spaces and runs depth-first search via backtracking.

### Initializing the State Space
* **`board` (`list[list[str]]`):** An $n \times n$ matrix initialized to `"."`.
* **`solutions` (`list`):** Stores completed valid board layouts.
* **`cols` (`set`):** Tracks which column indices currently contain a queen.
* **`diag1` (`set`):** Tracks active major diagonals using the mathematical invariant $(r - c)$.
* **`diag2` (`set`):** Tracks active minor diagonals using the mathematical invariant $(r + c)$.
* **`step = [0]`:** A single-element mutable list acting as a step counter across recursive scopes (avoiding Python scoping restrictions with primitive integers).

---

## 5. Step-by-Step Backtracking Cycle: `backtrack(r)`

The recursive function processes the board one row at a time, where $r$ denotes the current row index ($0$ to $n$).

### Step A: Base Case (Solution Found)
```python
if r == n:
    solutions.append([" ".join(row) for row in board])
    print(f"*** FOUND SOLUTION #{len(solutions)} ***")
    print_board(board)
    return
```
* **Trigger:** $r$ reaches $n$, meaning rows $0$ through $n - 1$ have each successfully received a non-conflicting queen.
* **Action:** Deep-copies the current board configuration into `solutions`, outputs the success marker with the full board layout, and returns to pop this frame from the call stack.

### Step B: Exploration & Conflict Checking (Pruning)
```python
for c in range(n):
    if c in cols or (r - c) in diag1 or (r + c) in diag2:
        continue
```
* The loop iterates through every column $c \in [0, n - 1]$.
* **Pruning Logic:** Before placing a queen, it performs an $\mathcal{O}(1)$ membership check on the three sets:
  * `c in cols`: Another queen already threatens this column.
  * `(r - c) in diag1`: Another queen occupies the same $\backslash$ diagonal.
  * `(r + c) in diag2`: Another queen occupies the same $/$ diagonal.
* If any condition is `True`, that entire subtree is pruned (`continue`), bypassing all invalid downstream configurations.

### Step C: State Modification (Forward Step)
```python
board[r][c] = "Q"
cols.add(c)
diag1.add(r - c)
diag2.add(r + c)
step[0] += 1
print(f"[Step {step[0]}] Place Queen at ({r}, {c}):")
print_board(board)
```
When a valid cell $(r, c)$ is found:
* `board[r][c]` changes from `"."` $\rightarrow$ `"Q"`.
* Column $c$ is marked active in `cols`.
* Diagonal $(r - c)$ is registered in `diag1`.
* Diagonal $(r + c)$ is registered in `diag2`.
* The move counter increments, and the resulting board state prints to the console.

### Step D: Recursive Descent
```python
backtrack(r + 1)
```
Suspends execution at row $r$ and pushes a new stack frame for row $r + 1$, repeating the search for the next queen.

### Step E: State Restoration (Backtracking Step)
```python
board[r][c] = "."
cols.remove(c)
diag1.remove(r - c)
diag2.remove(r + c)
step[0] += 1
print(f"[Step {step[0]}] Backtrack from ({r}, {c}):")
print_board(board)
```
Triggered when downstream exploration hits a dead end (or after returning from a discovered solution):
* `board[r][c]` is reset from `"Q"` $\rightarrow$ `"."`.
* $c$ is discarded from `cols`.
* $(r - c)$ is discarded from `diag1`.
* $(r + c)$ is discarded from `diag2`.
* The backtrack event prints to the console.
* The loop advances to test the next column $c + 1$ in row $r$.

---

## 6. Data Structure State Transitions

The following lifecycle traces how data structures transform during a placement and rollback on a $4 \times 4$ board at coordinate $(1, 3)$:

| Phase | `board[1][3]` | `cols` | `diag1` ($r - c$) | `diag2` ($r + c$) | Call Stack |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pre-Placement** | `"."` | $\{1\}$ | $\{0 - 1\} = \{-1\}$ | $\{0 + 1\} = \{1\}$ | `backtrack(1)` active |
| **Placement** | `"Q"` | $\{1, \mathbf{3}\}$ | $\{-1, \mathbf{-2}\}$ | $\{1, \mathbf{4}\}$ | Pushes `backtrack(2)` |
| **Dead End / Return** | `"Q"` | $\{1, 3\}$ | $\{-1, -2\}$ | $\{1, 4\}$ | Pops back to `backtrack(1)` |
| **Backtrack** | `"."` | $\{1\}$ *(3 removed)* | $\{-1\}$ *(-2 removed)* | $\{1\}$ *(4 removed)* | Advances to $c = 4$ *(loop terminates)* |


## Verification:

Verification happens through two distinct mechanisms: structural progression handles the rows, while mathematical hash sets handle the columns and diagonals.

---

### 1. How Rows Are Verified (Structural Guarantee)

The algorithm never has to check whether two queens share the same row:

* The recursive parameter `r` directly dictates the current row (`backtrack(r)`).
* The algorithm only ever places one queen at `(r, c)`, and immediately calls `backtrack(r + 1)` to advance to the next row.
* Because every level in the recursive call stack corresponds strictly to a unique row index, a row collision is physically impossible by design.

---

### 2. How Columns Are Verified (`cols` Set)

Vertical attacks are verified in $\mathcal{O}(1)$ time using the `cols` hash set:

* **Before placement:** The condition `c in cols` checks if the candidate column $c$ has already been claimed by a queen placed in any previous row.
* **If present (`True`):** The column is under attack; the algorithm skips it via `continue`.
* **If absent (`False`):** The column is safe. It is recorded with `cols.add(c)`.
* **When backtracking:** Once all sub-branches under that choice are explored, `cols.remove(c)` frees the column back up for subsequent placements.

---

### 3. How Diagonals Are Verified (`diag1` and `diag2` Sets)

Queens also attack along diagonals. Instead of scanning upward diagonally across the grid with a `while` loop, the algorithm relies on two coordinate invariants:

#### Major Diagonals ($\backslash$ top-left to bottom-right)
Every square lying on the exact same downward-sloping diagonal shares the identical difference between its row and column coordinates:

$$r - c = \text{constant}$$

* **Example:** Coordinates $(0, 0)$, $(1, 1)$, $(2, 2)$ all produce $r - c = 0$. Coordinates $(0, 2)$, $(1, 3)$ both yield $r - c = -2$.
* **Check:** `(r - c) in diag1`

#### Minor Diagonals ($/$ top-right to bottom-left)
Every square lying on the exact same upward-sloping diagonal shares the identical sum of its row and column coordinates:

$$r + c = \text{constant}$$

* **Example:** Coordinates $(0, 3)$, $(1, 2)$, $(2, 1)$, $(3, 0)$ all produce $r + c = 3$.
* **Check:** `(r + c) in diag2`

---
