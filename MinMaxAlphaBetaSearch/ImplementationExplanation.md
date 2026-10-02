# Minimax & Alpha-Beta Pruning Implementation Guide
Example Taken:
Depth:4
Branching Factor: 2
16 leaf values separated by spaces:
10 11 9 12 14 15 13 14 5 2 4 1 3 22 20 21

SEARCH TREE STRUCTURE

|-- MAX
    |-- MIN
        |-- MAX
            |-- MIN
                \-- Leaf = 10
                \-- Leaf = 11
            |-- MIN
                \-- Leaf = 9
                \-- Leaf = 12
        |-- MAX
            |-- MIN
                \-- Leaf = 14
                \-- Leaf = 15
            |-- MIN
                \-- Leaf = 13
                \-- Leaf = 14
    |-- MIN
        |-- MAX
            |-- MIN
                \-- Leaf = 5
                \-- Leaf = 2
            |-- MIN
                \-- Leaf = 4
                \-- Leaf = 1
        |-- MAX
            |-- MIN
                \-- Leaf = 3
                \-- Leaf = 22
            |-- MIN
                \-- Leaf = 20
                \-- Leaf = 21

RESULTS

Minimax Root Value    : 10
Alpha-Beta Root Value : 10

PRUNING DETAILS

 * Skipped branch due to: Alpha cutoff at MIN
 * Skipped branch due to: Beta cutoff at MAX
 * Skipped branch due to: Alpha cutoff at MIN
 * Skipped branch due to: Alpha cutoff at MIN
 * Skipped branch due to: Alpha cutoff at MIN

COMPARISON

Minimax nodes checked    : 31
Alpha-Beta nodes checked : 18
Nodes saved (pruned)     : 13
Efficiency improvement   : 41.94 %

## 1. The Underlying Data Structures & How They Evolve

Before looking at the functions, it is essential to understand the two primary data representations used:

### A. The Raw List (`leaf_values`)
* **Type:** Standard Python dynamic array/list (e.g., `[10, 11, 9, 12, ...]`).
* **Modification:** Acts as an ordered queue via `.pop(0)`. Every time the builder reaches the bottom depth, the leftmost number is removed from the front of the list and converted into a terminal state.

### B. The Recursive Tree (Nested Dictionaries)
* **Internal Nodes:** Stored as dictionaries:
  ```python
  {
      "is_max": True,   # Boolean: True for MAX's turn, False for MIN's turn
      "children": [...] # List containing child dictionaries or terminal integers
  }
  ```
* **Leaf (Terminal) Nodes:** Plain Python integers (e.g., `10`, `9`).

#### Visual Representation in Memory:
```text
Root (dict: is_max=True)
 ├── Child 1 (dict: is_max=False)
 │    ├── Subchild A (dict: is_max=True) -> ... -> Leaf (int: 10)
 │    └── Subchild B (dict: is_max=True) -> ... -> Leaf (int: 11)
 └── Child 2 (dict: is_max=False)
      └── ...
```

---

## 2. Function-by-Function Detailed Explanation

```text
                          ┌──────────────┐
                          │    main()    │
                          └──────┬───────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌──────────────────┐    ┌─────────────────┐    ┌──────────────────┐
│input_and_build_  │    │     minmax()    │    │   alphabeta()    │
│     tree()       │    └─────────────────┘    └──────────────────┘
└──────────────────┘             │                       │
                                 └───────────┬───────────┘
                                             ▼
                                    ┌─────────────────┐
                                    │    display()    │
                                    └─────────────────┘
```

---

### Function 1: `input_and_build_tree()`

```python
def input_and_build_tree():
    ply = int(input("Enter tree depth / ply (must be > 3, e.g., 4): "))
    while ply <= 3:
        ply = int(input("Enter tree depth / ply (e.g., 4): "))

    branching = int(input("Enter branching factor (e.g., 2): "))
    total_leaves = branching ** ply
    ...
```

* **Purpose:** Handles console input validation and constructs the full game tree in memory from the top down.
* **Flow & Logic:**
  * Prompts for `ply` (depth) and enforces `ply > 3` using a `while` loop (satisfying requirement 3 of your assignment).
  * Prompts for `branching` (e.g., $2$ for binary).
  * Calculates total leaves needed:
    $$\text{total\_leaves} = \text{branching}^{\text{ply}}$$
  * Reads the input string, splits it on whitespace, and appends each number as an `int` into `leaf_values`.
* **Tree Construction (`build(current_depth, is_max)`):**
  * **Base Case (`current_depth == ply`):** Recursion has hit the bottom layer. It calls `leaf_values.pop(0)`, which removes the first integer from the list and returns it directly as a leaf node.
  * **Recursive Step:**
    1. Creates an empty `children = []` list.
    2. Loops `branching` times.
    3. Calls `build(current_depth + 1, not is_max)` for each child. Passing `not is_max` automatically flips the role: Depth 0 is MAX (Root), Depth 1 is MIN, Depth 2 is MAX, Depth 3 is MIN, and Depth 4 holds leaves.
    4. Packages the node into a dictionary `{"is_max": is_max, "children": children}` and returns it up the stack.

---

### Function 2: `minmax(node)`

```python
def minmax(node):
    global minimax_visited
    minimax_visited = minimax_visited + 1

    if type(node) is int:
        return node
    ...
```

* **Purpose:** Implements the pure, unpruned Minimax decision rule via Depth-First Search (DFS).
* **Flow & Logic:**
  * **Visit Tracking:** Increments `minimax_visited` by $1$ every time any node (internal or leaf) is touched.
  * **Base Case:** Evaluates `type(node) is int`. If true, this is a terminal state, and it returns the raw numeric utility upward.
  * **MAX Player Evaluation (`node["is_max"] is True`):**
    1. Sets `best = -9999` ($-\infty$).
    2. Loops through every child in `node["children"]` without skipping.
    3. Recursively calls `val = minmax(child)`.
    4. If `val > best`, updates `best = val`.
    5. Returns `best` (the maximum utility MAX can achieve).
  * **MIN Player Evaluation (`else`):**
    1. Sets `best = 9999` ($+\infty$).
    2. Loops through every child in `node["children"]`.
    3. Recursively calls `val = minmax(child)`.
    4. If `val < best`, updates `best = val`.
    5. Returns `best` (the minimum utility MIN will restrict MAX to).
* **Data Flow:** Values flow downward via recursive function calls until leaves are reached, then propagate upward as return values, picking $\max$ or $\min$ at alternating levels.

---

### Function 3: `alphabeta(node, alpha, beta)`

```python
def alphabeta(node, alpha, beta):
    global alphabeta_visited
    alphabeta_visited = alphabeta_visited + 1

    if type(node) is int:
        return node
    ...
```

* **Purpose:** Computes the optimal game decision while cutting off (pruning) branches that cannot influence the final outcome.
* **Flow & Logic:**
  * **Visit Tracking:** Increments `alphabeta_visited` by $1$.
  * **Base Case:** Returns `node` immediately if it is a terminal integer.
  * **MAX Player Turn (`node["is_max"] is True`):**
    1. Sets `best = -9999`.
    2. Loops through children using index `i`: `for i in range(len(children)):`.
    3. Recursively evaluates `val = alphabeta(child, alpha, beta)`.
    4. Updates `best = max(best, val)`.
    5. Updates `alpha = max(alpha, best)`: MAX records the best score guaranteed so far along this path.
    6. **Cutoff Check (`if beta <= alpha`):**
       * If true, MIN's ancestor already has an option guaranteeing a lower or equal value elsewhere. MIN will never let play reach this branch.
       * A second loop (`for unvisited in children[i + 1:]:`) iterates over the remaining sibling branches that were never evaluated and logs them into `pruned_list`.
       * `break` terminates the loop immediately, skipping further recursive calls for this node.
  * **MIN Player Turn (`else`):**
    1. Sets `best = 9999`.
    2. Loops through children.
    3. Recursively evaluates `val = alphabeta(child, alpha, beta)`.
    4. Updates `best = min(best, val)`.
    5. Updates `beta = min(beta, best)`: MIN records the lowest score it can force MAX to take.
    6. **Cutoff Check (`if beta <= alpha`):**
       * If true, MAX's ancestor already secured a higher or equal score on an earlier branch. MAX will never pick the move leading to this MIN node.
       * The remaining siblings (`children[i + 1:]`) are logged into `pruned_list`.
       * `break` exits the loop immediately.

---

### Function 4: `display(tree, mm_result, ab_result)`

* **Purpose:** Formats and prints all four deliverables required by the assignment.
* **Flow & Logic:**
  * **`show_tree(node, depth)`:** A recursive printer. Uses string indentation (`"    " * depth`) to print node roles (`|-- MAX` or `|-- MIN`) and leaf utilities (`\-- Leaf = X`).
  * **Prints Final Utilities:** Displays `mm_result` and `ab_result` side by side to prove both algorithms yield the same game-theoretic value.
  * **Prints Pruned List:** Loops through `pruned_list` and prints every cut that occurred, specifying whether it was an Alpha or Beta cutoff.
  * **Comparative Analysis:**
    $$\text{Nodes Saved} = \text{minimax\_visited} - \text{alphabeta\_visited}$$
    $$\text{Efficiency \%} = \left(\frac{\text{Nodes Saved}}{\text{minimax\_visited}}\right) \times 100$$

---

### Function 5: `main()`

```python
def main():
    tree = input_and_build_tree()
    mm_res = minmax(tree)
    ab_res = alphabeta(tree, -9999, 9999)
    display(tree, mm_res, ab_res)
```

* **Purpose:** The entry point and conductor of the program.
* **Execution Sequence:**
  1. Calls `input_and_build_tree()` to construct the tree from user inputs.
  2. Calls `minmax(tree)` to perform the baseline full search.
  3. Calls `alphabeta(tree, -9999, 9999)` with initial boundaries $\alpha = -\infty$ and $\beta = +\infty$.
  4. Calls `display()` to output the tree, terminal states, pruned branches, and comparative metrics.