# Greedy Best-First Search (GBFS):

Greedy Best-First Search (GBFS) is an informed search algorithm designed to traverse a graph or tree toward a target goal node as quickly as possible. It is called Greedy because at every decision point, it evaluates all currently reachable unvisited nodes and expands the one that appears closest to the goal according to a heuristic evaluation function $h(n)$.

## The Real-World Analogy: The "Sticky Note" Treasure Hunt

Imagine you are in a massive, unfamiliar library trying to find an Exit Door (the Goal).
* Heuristic Value $h(n)$: From any room you stand in, you look through a window or hallway sign that shows an estimated direct line-of-sight distance to the exit (e.g., "Looks like ~30 meters away"). You have no idea if walls, locked doors, or winding staircases lie ahead; you only trust that estimate.
* The Clipboard (open_list): You carry a clipboard with sticky notes. Every time you stand at a doorway with multiple paths branching out, you write down each adjacent room and its estimated distance, then stick them onto your clipboard:[Room A, ~40m], [Room B, ~15m], [Room C, ~60m]
* Greedy Decision: You sort your sticky notes and always walk into the room with the smallest distance number (Room B, ~15m).
* The Logbook (visited set): To ensure you don't run in circles between rooms, you stamp your current room in a logbook.
* Backtracking Safety Net: Suppose Room B leads directly into a dead-end storage closet. You don't get trapped. You simply pull out your clipboard, look at the remaining sticky notes you wrote down earlier (Room A at ~40m and Room C at ~60m), and immediately backtrack to explore Room A.

## The Core Objective:
* Primary Goal: Reach the destination node while minimizing the total number of node expansions.
* Evaluation Function: Uses strictly $f(n) = h(n)$, where $h(n)$ is the estimated cost or distance from node $n$ to the goal.
* Key Characteristic: It completely ignores the actual cost accumulated from the start node ($g(n)$). It focuses exclusively on the estimated remaining distance ahead.

## Core Concepts Used & Applied
1. Informed / Heuristic Search:
    Unlike uninformed searches (like standard Breadth-First Search or Depth-First Search) that blindly search every branch, GBFS uses domain knowledge ($h(n)$) to guide its path toward the target.
2. Greedy Strategy:
    At every step, the algorithm chooses what looks best right now ($f(n) = h(n)$) without considering the total cumulative path cost already spent.
3. Global Frontier Management:
    The frontier (open_list) preserves all discovered but unexplored alternative paths. This grants GBFS the ability to perform backtracking whenever an aggressive greedy path hits a dead end.
4. State Memoization (Cycle Detection):
    Using a hash-set (visited) guarantees $O(1)$ lookups to skip redundant paths and prevent infinite loops in cyclic graphs.

## Process Flow and Step by step example:

┌───────────────────────────────┐
               │         Start Search          │
               │   Push (h(start), [start])    │
               │         into Open List        │
               └───────────────┬───────────────┘
                               │
                               ▼
                   ┌───────────────────────┐
             ┌────►│  Is Open List Empty?  ├──────(Yes)─────► [ Terminate: No Path Found ]
             │     └───────────┬───────────┘
             │                 │ (No)
             │                 ▼
             │     ┌───────────────────────┐
             │     │   Sort Open List by   │
             │     │      h(n) Ascending   │
             │     └───────────┬───────────┘
             │                 │
             │                 ▼
             │     ┌───────────────────────┐
             │     │   Pop First Item      │
             │     │ (Lowest Heuristic)    │
             │     │  Current Node = Path  │
             │     └───────────┬───────────┘
             │                 │
             │                 ▼
             │     ┌───────────────────────┐
             │     │   Is Current Node ==  ├──────(Yes)─────► [ Terminate: Goal Reached! ]
             │     │         Goal?         │                  [ Return Current Path   ]
             │     └───────────┬───────────┘
             │                 │ (No)
             │                 ▼
             │     ┌───────────────────────┐
             │     │ Node in Visited Set?  ├──────(Yes)─────► [ Ignore & Continue ]
             │     └───────────┬───────────┘
             │                 │ (No)
             │                 ▼
             │     ┌───────────────────────┐
             │     │  Add Node to Visited  │
             │     └───────────┬───────────┘
             │                 │
             │                 ▼
             │     ┌───────────────────────┐
             │     │ For each unvisited    │
             │     │ neighbor:             │
             │     │ Append to Open List:  │
             │     │ (h(nbr), Path + [nbr])│
             │     └───────────┬───────────┘
             │                 │
             └─────────────────┘

Consider the following directed graph with heuristic estimates to the goal G:
    [S] (h=10)
       /   \
 (h=8)[A]   [B] (h=5)
     / \     / \
(h=7)[C] [D] [E] [G] (h=0) <-- Goal
        (h=3) (h=6)
          
Nodes & Heuristics:
$h(S) = 10$
$h(A) = 8$
$h(B) = 5$
$h(C) = 7$
$h(D) = 3$
$h(E) = 6$
$h(G) = 0$
Start Node: S
Goal Node: G

### Step 1: Initialize
* **Action:** Place the start node $S$ into the frontier.
* **`open_list`:** `[(10, ['S'])]`
* **`visited`:** `{}`


### Step 2: Expand S
* **Pop lowest $h(n)$:** `(10, ['S'])` $\rightarrow$ Current node is $S$.
* **Goal Check:** $S \neq G$
* **Mark visited:** `visited = {'S'}`
* **Discover neighbors of $S$:**
  * **Neighbor A:** $h(A) = 8 \rightarrow$ path `['S', 'A']`
  * **Neighbor B:** $h(B) = 5 \rightarrow$ path `['S', 'B']`
* **Update `open_list`:** `[(8, ['S', 'A']), (5, ['S', 'B'])]`
* **Sort `open_list`:** `[(5, ['S', 'B']), (8, ['S', 'A'])]`



### Step 3: Expand B
* **Pop lowest $h(n)$:** `(5, ['S', 'B'])` $\rightarrow$ Current node is $B$.
* **Goal Check:** $B \neq G$
* **Mark visited:** `visited = {'S', 'B'}`
* **Discover neighbors of $B$:**
  * **Neighbor E:** $h(E) = 6 \rightarrow$ path `['S', 'B', 'E']`
  * **Neighbor G:** $h(G) = 0 \rightarrow$ path `['S', 'B', 'G']`
* **Update `open_list`:** `[(8, ['S', 'A']), (6, ['S', 'B', 'E']), (0, ['S', 'B', 'G'])]`
* **Sort `open_list`:** `[(0, ['S', 'B', 'G']), (6, ['S', 'B', 'E']), (8, ['S', 'A'])]`



### Step 4: Expand G & Goal Reached
* **Pop lowest $h(n)$:** `(0, ['S', 'B', 'G'])` $\rightarrow$ Current node is $G$.
* **Goal Check:** $G = G \rightarrow$ **Success!**
* **Returned Solution Path:** $S \rightarrow B \rightarrow G$
* **Total Expansions:** 3 nodes ($S$, $B$, $G$)

---

## Why the Algorithm Works
* Heuristic Gradient Descent: By always expanding the node with the lowest $h(n)$, the algorithm acts like a gradient descent optimizer, continually moving in the direction of the steepest estimated reduction in distance to the goal.
* Global Backtracking Capability: Because open_list retains all previously encountered, unexpanded branch points, hitting a dead end (a node with no unvisited neighbors) does not crash or terminate the search. The algorithm naturally steps back to the next best globally available node on the subsequent iteration.
* Target Reachability Guarantee: In any finite graph with cycle checking, GBFS will always terminate. If a path exists and no heuristics are $\infty$, it will find a valid path to the goal.

## example code:
```python

def greedy_best_first_search(graph, heuristics, start, goal):
    # open_list stores tuples of (heuristic_value, [traversal_path])
    open_list = [(heuristics[start], [start])]
    visited = set()
    step = 1

    print("\n" + "=" * 25 + " BEST FIRST SEARCH (GBFS) " + "=" * 25)

    while open_list:
        # Step 1: Sort open list ascending by heuristic value h(n)
        open_list.sort(key=lambda item: item[0])

        # Step 2: Pop the node with the lowest heuristic value (index 0)
        h_val, current_path = open_list.pop(0)
        current_node = current_path[-1]

        print(f"\n[Step {step}] Visiting Node: '{current_node}' (h = {h_val})")
        print(f"  Current Path   : {' -> '.join(current_path)}")
        step += 1

        # Step 3: Check goal condition
        if current_node == goal:
            print(f"\n>>> GOAL '{goal}' REACHED! <<<")
            return current_path

        # Step 4: Expand unvisited neighbors
        if current_node not in visited:
            visited.add(current_node)
            discovered = []

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    new_path = current_path + [neighbor]
                    open_list.append((heuristics[neighbor], new_path))
                    discovered.append(f"{neighbor}(h={heuristics[neighbor]})")

            print(f"  Visited Set    : {visited}")
            print(f"  Added to Open  : {discovered if discovered else 'None (Dead end)'}")
            print(f"  Remaining Open : {[(cost, path[-1]) for cost, path in open_list]}")

    print(f"\n>>> GOAL '{goal}' UNREACHABLE <<<")
    return None

```

## Code Flow:

Initialization:

open_list = [(heuristics[start], [start])]: The frontier storing tuples of (heuristic_score, path_list).

visited = set(): A hash set storing explored nodes to avoid infinite loops and redundant exploration.

Sorting the Frontier (Simulated Priority Queue):
Python
open_list.sort(key=lambda item: item[0])
h_val, current_path = open_list.pop(0)

open_list.sort(key=lambda item: item[0]) sorts elements in ascending order by heuristic value $h(n)$.
.pop(0) removes and returns the first element, guaranteeing that the globally lowest $h(n)$ candidate is evaluated next.

Neighbor Expansion & State Update:

visited.add(current_node) marks the current node as closed.

new_path = current_path + [neighbor] generates a new list instance, preserving historical steps for the path without mutating existing paths in open_list.

open_list.append(...) inserts newly discovered paths into the frontier pool to be sorted in the next loop cycle.


### Algorithmic Trade-offs & Limitations:
Strength
High Search Speed: Reaches the goal with significantly fewer node expansions than standard BFS or DFS.
Low Memory Footprint (vs. BFS): Does not explore every branch uniformly at each depth level.

Limitation
Suboptimal Paths: It ignores the true cost incurred so far ($g(n)$). If an initial step has a misleadingly low heuristic, GBFS will commit to it, even if the total path length is suboptimal.
Susceptible to Local Minima: Heuristic plateaus or deceptive local minima can force unnecessary exploration of dead-end subtrees before falling back.

## Key Applications and Real-World Use Cases:
Greedy Best-First Search (GBFS) is applied in scenarios where finding a fast, approximate solution is prioritized over finding the mathematically shortest or least expensive path.
* Video Game AI & Non-Player Character (NPC) Pathfinding:
    Fast real-time navigation for enemies or companion characters navigating large open maps toward the player when computing an optimal $A^*$ path is too computationally expensive per frame.
* GPS Route Planning & Quick Direction Estimation:
    Providing an instantaneous rough navigation route or initial estimate before background threads compute the fully optimized turn-by-turn route.
* Robotics & Spatial Navigation:
    Autonomous mobile robots with limited onboard compute navigating obstacle-rich terrain toward a target beacon using Euclidean or Manhattan distance estimates.
* Automated Planning & Web Crawling:
    Targeted Web Crawlers (Focused Crawling): Crawling engines prioritizing hyperlinks that score highest on a relevance/keyword similarity heuristic to reach domain-specific pages faster.
    AI Planning Problems: Navigating large state spaces to find a valid sequence of actions to reach a goal configuration without evaluating all possible permutations.
* Computer-Aided Design (CAD) & Circuit Routing:
    Rapid initial wire routing on printed circuit boards (PCBs) or VLSI designs where an approximate connection path is generated first and refined later.

## Critical Failsafes:

**Critical Failsafes in Best-First Search (GBFS)** are safeguards implemented to prevent infinite loops, unhandled edge cases, runtime crashes, and resource exhaustion.


1. The Closed/Visited Set (Cycle Prevention)

* **The Risk:** Cyclic graphs (e.g., $A \rightarrow B \rightarrow A$) or bidirectional edges can cause the search to bounce infinitely between low-heuristic nodes.
* **The Failsafe:** Maintain a `visited = set()` and enforce a membership check before adding nodes to the frontier or expanding them.

```python
# Check membership before processing
if current_node not in visited:
    visited.add(current_node)
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            open_list.append((heuristics[neighbor], current_path + [neighbor]))

```

2. Missing Key / Disconnected Node Safeguards

* **The Risk:** In user-defined graphs, leaf nodes (nodes with 0 outgoing edges) often do not appear as keys in adjacency dictionaries, triggering a `KeyError`.
* **The Failsafe:** Use `.get(current_node, [])` instead of direct indexing (`graph[current_node]`) to return an empty list gracefully on terminal/leaf nodes.

3. Tie-Breaking Mechanism in the Open List

* **The Risk:** If two candidate paths have the exact same heuristic score (e.g., $h(A) = 4, h(B) = 4$), Python tries to compare the second element of the tuple (`current_path`). If elements cannot be compared or paths have different structures, it creates non-deterministic traversal or ordering errors.
* **The Failsafe:** Include an incremental insertion counter or secondary sorting key to resolve ties deterministically without comparing raw node objects:

```python
# Store: (heuristic, entry_count, path)
count = 0
open_list.append((heuristics[neighbor], count, new_path))
count += 1

```

4. Bounded Frontier / Iteration Caps (Memory Exhaustion)

* **The Risk:** On infinite or extremely large state spaces, `open_list` can grow until memory limits are exceeded ($O(V)$ memory complexity).
* **The Failsafe:** Set a maximum iteration counter (`max_steps`) or a cap on `open_list` size:

```python
max_steps = 10000
step = 0

while open_list and step < max_steps:
    step += 1
    # ... search logic ...

if step >= max_steps:
    print("Search aborted: Exceeded maximum step limit.")

```

5. Start and Goal Existence Validation

* **The Risk:** Providing a `start` or `goal` node that was never declared in the graph or heuristic table leads to an immediate crash during runtime initialization.
* **The Failsafe:** Validate inputs before running the search loop:

```python
if start not in heuristics or goal not in heuristics:
    raise ValueError("Start or Goal node missing from heuristic definitions.")

```
---