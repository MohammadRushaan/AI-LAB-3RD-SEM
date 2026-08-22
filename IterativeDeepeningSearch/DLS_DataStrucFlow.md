# Depth-Limited Search (DLS)

DLS acts as a bounded exploration worker. It performs standard Depth-First Search with one critical constraint: a depth counter (`limit`).

* **Explores Deeply:** Travels as deep into a single branch as possible before backtracking.
* **Enforces a Boundary:** When the recursion reaches the specified depth limit (`limit == 0`), it halts further descent down that branch, reports that the target was not found at this level, and backtracks to inspect unvisited sibling branches.
* **Builds Intermediate States:** Reports which nodes were visited during this specific depth round and returns `True` only if the exact target is reached within the allotted depth budget.

---

## Data Structures Used and Their Purpose

| Data Structure | Code Representation | Purpose & Function |
| :--- | :--- | :--- |
| **Adjacency List (Hash Map of Lists)** | `collections.defaultdict(list)` | Stores graph/tree topology where each key is a parent node and the value is a list of its directly connected children. Enables $O(1)$ lookup for node neighbors. |
| **Active Branch (Dynamic Array / List)** | `path = []` | Stores the current ancestor lineage from the start node down to the active node. Used to extract the final route and prevent cyclic loops (`neighbor not in path`). |
| **History Log (Dynamic Array / List)** | `visited_order = []` | Captures every node expanded during the current depth pass to print intermediate execution steps. |
| **System Call Stack (LIFO)** | Handled automatically by Python recursion | Maintains execution context (local variables, return addresses, remaining limit) across nested function calls, eliminating the need to manage a manual stack. |

---

## How DLS is Implemented in Code

The implementation relies on three structural components:

### 1. State Tracking and Base Checks
```python
visited_order.append(current_node)
path.append(current_node)

if current_node == goal_node:
    return True

if limit <= 0:
    path.pop()  # Backtrack: remove node because limit is exhausted
    return False

```
---
## Data Structure Mutation:

To understand how data structures mutate during execution, trace the state of these three core structures:

* **Call Stack (Recursion Frames):** Manages the active function scope, local variables, and return positions.
* **`path` (Branch Tracker):** Holds the exact sequence of nodes from root to the active node (`path.append()` pushes, `path.pop()` removes).
* **`visited_order` (Log List):** Monotonically grows with every visit to record the overall exploration history.

### Step-by-Step Mutation Table (Example Tree: Start A, Goal E, Depth Limit 2)

| Step # | Event / Line Executed | Call Stack State | `path` List | `visited_order` List | Action Type |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Enter `dls(A, limit=2)` | `[dls(A, 2)]` | `['A']` | `['A']` | Push to Stack & Path |
| **2** | Check Goal (A != E) $\rightarrow$ Call Child B | `[dls(A, 2), dls(B, 1)]` | `['A', 'B']` | `['A', 'B']` | Push child B |
| **3** | Check Goal (B != E) $\rightarrow$ Call Child D | `[dls(A, 2), dls(B, 1), dls(D, 0)]` | `['A', 'B', 'D']` | `['A', 'B', 'D']` | Push child D |
| **4** | D: Goal check fails $\rightarrow$ `limit <= 0` triggers | `[dls(A, 2), dls(B, 1), dls(D, 0)]` | `['A', 'B']` | `['A', 'B', 'D']` | `path.pop()` (D removed) |
| **5** | Return `False` from `dls(D)` | `[dls(A, 2), dls(B, 1)]` | `['A', 'B']` | `['A', 'B', 'D']` | Stack Pop (D frame exits) |
| **6** | B moves to next child $\rightarrow$ Call E | `[dls(A, 2), dls(B, 1), dls(E, 0)]` | `['A', 'B', 'E']` | `['A', 'B', 'D', 'E']` | Push child E |
| **7** | E: `current_node == goal_node` matches! | `[dls(A, 2), dls(B, 1), dls(E, 0)]` | `['A', 'B', 'E']` | `['A', 'B', 'D', 'E']` | Match Found (No pop) |
| **8** | Return `True` up the call stack | `[]` (unwinds to driver) | `['A', 'B', 'E']` | `['A', 'B', 'D', 'E']` | Preserve & Output Path |


## Behavior Rules of Each Structure Per Check
* visited_order (Append-Only):
    On every visit: Appends the node immediately.
    On backtrack / fail: Does not pop. It preserves the complete chronological history of visited nodes.
* path (Mirror of Call Stack):
    On downward step: path.append(node) mirrors entering a new recursive stack frame.
    On dead-end or cutoff (limit <= 0 or no remaining children): path.pop() runs immediately, rewinding the path back to the parent.
    On goal match: path.pop() is bypassed, keeping the exact path from root to goal intact.
* Call Stack (Automatic Memory Reclamation):
        Allocates local variables (current_node, remaining limit) per frame.
        When a frame returns False, Python drops that frame from memory, ensuring space complexity stays bounded at $O(\text{depth})$.