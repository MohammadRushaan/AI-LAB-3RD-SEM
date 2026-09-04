### What is Backtracking?

**Backtracking** is a systematic algorithmic technique for solving constraint satisfaction problems by building candidate solutions incrementally and abandoning a candidate (**"backtracking"**) as soon as it determines that the candidate cannot possibly lead to a valid final solution.

Think of it like navigating a maze: you walk forward down a path until you hit a dead end, step backward to the last fork in the road, and try an unexplored direction.

---

### The Core Mechanism: The 3-Step Recursive Contract

Every recursive backtracking cycle in the N-Queens problem follows the exact same three-part blueprint:

        [ Choose (r, c) ]
               │
               ▼
     [ Recurse: backtrack(r + 1) ]
        /                     \
  (Dead End)               (Solution)
      │                        │
      ▼                        ▼
 [ Un-choose ]            [ Save State ]

1. **Choose (Make a move):** 
   You place a queen at coordinate `(r, c)` and register its attack lines into tracking structures (`board`, `cols`, `diag1`, `diag2`).

2. **Explore (Recurse deeper):** 
   You call `backtrack(r + 1)` to solve the next row under the assumption that the current placement was correct.

3. **Un-choose (Backtrack / Undo):** 
   When `backtrack(r + 1)` returns—whether because all downstream attempts hit a dead end or because you finished finding a solution and want to discover other solutions—you **revert the state**:
   * Clear `board[r][c] = '.'`
   * Remove column `c` and diagonals `(r - c)` and `(r + c)` from the sets
   * Proceed to test column `c + 1`

---

### How It Works in N-Queens: Backtracking vs. Brute Force

Without backtracking, placing $N$ queens on an $N \times N$ board requires testing every possible combination:
* For an $8 \times 8$ board, pure brute force tests $\binom{64}{8} \approx 4.4 \times 10^9$ combinations.
* Even restricting to one queen per row yields $8^8 \approx 16.7 \times 10^6$ combinations.

Backtracking slashes this search space through **early pruning**:

                Row 0: Place (0, 0)
                           │
                   Row 1: Place (1, 2)
                           │
                   Row 2: DEAD END!
             (Columns 0, 1, 2, 3 all invalid)
                           │
                   [ BACKTRACK ] ──> Undo (1, 2)
                           │
                   Row 1: Try (1, 3) ...

As seen in Phase 1 of the trace:
* When row 2 has no safe squares after placing `(0, 0)` and `(1, 2)`, the algorithm **does not even touch row 3**.
* It immediately abandons that entire branch of the decision tree, saving hundreds of wasted checks.

---

### The Role of the Call Stack

Backtracking does not need an explicit list of historical states because it relies on the **Call Stack**:

* **Pushing onto the stack:** Every recursive step (`backtrack(r + 1)`) creates a new stack frame holding its own local loop counter (`c`). The parent frame sits suspended, waiting.
* **Popping off the stack:** When a dead end occurs, the function returns. Control seamlessly returns to the caller's frame at row $r$, immediately right after the line `backtrack(r + 1)`.
* Because the code right after that line is the **cleanup phase**, execution cleanly resets the board and continues the loop from where it left off.