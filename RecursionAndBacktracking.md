# Depth-First Search (DFS): Recursion and Backtracking

At its core, **Depth-First Search (DFS)** is a graph traversal algorithm that explores as deep as possible along each branch before turning back. 

To understand DFS fully, you need to understand how **Recursion** acts as the engine driving the exploration forward, and how **Backtracking** acts as the safety net that lets you step back and try other paths.

---

## 1. The Core Triad: DFS, Recursion, and Backtracking

| Concept | Role in Graph Traversal | Real-World Analogy |
| :--- | :--- | :--- |
| **DFS (Strategy)** | The high-level plan: "Keep going straight down a path until you hit a dead end, then try another." | Exploring a maze by hugging one wall until you reach a dead end. |
| **Recursion (Execution)** | The engine: Calling the same function on neighboring nodes to dive deeper into the graph. | Dropping breadcrumbs at every intersection as you go deeper. |
| **Backtracking (Recovery)** | The mechanism: Reverting to the previous state/node when a path is exhausted, allowing you to explore unvisited branches. | Following your breadcrumbs back to the last untried intersection after hitting a dead end. |

---

## 2. How the System Remembers: The Call Stack

When you implement DFS recursively, you rely on the programming language's internal **Call Stack**.

1. **Forward Step (Recursion):** When node `A` visits node `B`, `DFS(B)` is pushed onto the call stack. Node `A` stays paused in memory right where it called `B`.
2. **Dead End / Base Case:** When node `B` has no unvisited neighbors left, `DFS(B)` completes.
3. **Backward Step (Backtracking):** `DFS(B)` is popped off the stack. Control automatically returns to node `A`, right where it paused, allowing `A` to check its next neighbor `C`.

---

## 3. Standard DFS vs. Explicit Backtracking

It is important to distinguish between standard DFS and explicit decision-tree backtracking:

### Standard Graph DFS (Traversing Nodes)
* **Goal:** Visit every reachable node once.
* **State Handling:** Mark nodes as `visited`. Once a node is marked `visited`, it stays `visited` so you don't fall into infinite loops (cycles).
* **Backtracking Behavior:** Simply popping function calls off the call stack when a path finishes.

### Backtracking DFS (Finding Paths/Combinations)
* **Goal:** Find paths, solve puzzles (e.g., N-Queens, Sudoku, or finding all simple paths between source and target).
* **State Handling:** Mark a node as `visited`, explore all paths through it, and then **unmark** it (`visited.remove(node)`) as you backtrack.
* **Why unmark?** So that the node becomes available again for different paths originating from a different branch.