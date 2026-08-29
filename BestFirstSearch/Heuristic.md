A **heuristic** is a computational "rule of thumb," educated guess, or mathematical shortcut used by search algorithms to make quick, informed decisions.

In pathfinding, a heuristic function—denoted as $h(n)$—estimates the remaining cost or physical distance from any given node $n$ to the designated goal.

### How the Heuristic is Applied Here

In this implementation of **Greedy Best-First Search (GBFS)**, the heuristic value acts as the single driving force for every navigation decision:

1. **Frontier Scoring:** When candidate nodes are discovered, their heuristic values are retrieved from the `heuristics` lookup table and bundled with the traversal path:
```python
open_list.append((heuristics[neighbor], new_path))

```

2. **Prioritization Ordering:** The search space is sorted in ascending order of $h(n)$:
```python
open_list.sort(key=lambda item: item[0])

```

3. **Greedy Selection:** The algorithm always extracts the head of the sorted list (`open_list.pop(0)`), picking the node that has the lowest estimated distance to the target.


### Why Heuristics are Used

* **Eliminating Blind Exploration:** Uninformed search algorithms like Breadth-First Search (BFS) or Depth-First Search (DFS) search in every direction uniformly. A heuristic acts like a compass, directing expansion toward the target to avoid exploring useless branches.
* **Pruning the Search Space:** By focusing on paths where $h(n)$ decreases rapidly, the search avoids large sections of the graph, reducing both runtime and CPU cycles.
* **Handling Massive Scale:** In large graph networks (e.g., GPS road maps with millions of intersections), exhaustive exploration is computationally impossible in real-time. A heuristic provides a near-instant estimate of which direction is worth exploring first.

### Common Real-World Heuristic Metrics

In 2D/3D physical spatial graphs, heuristics are usually calculated via geometric formulas:

* **Euclidean Distance (Straight-line distance "as the crow flies"):**

$$h(n) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

*Best for:* Open spaces where movement is allowed in any continuous angle.
* **Manhattan Distance (Grid / City-block distance):**

$$h(n) = \vert{}x_2 - x_1\vert{} + \vert{}y_2 - y_1\vert{}$$

*Best for:* Grid-based maps where movement is restricted to 4 cardinal directions (Up, Down, Left, Right).
* **Chebyshev / Diagonal Distance:**

$$h(n) = \max(\vert{}x_2 - x_1\vert{}, \vert{}y_2 - y_1\vert{})$$

*Best for:* Grid environments where 8-directional movement (including diagonals) is permitted.


### The Trade-off: Optimality vs. Speed

A heuristic offers speed at the expense of guaranteed accuracy:

* **The Risk of Being Greedy:** If a path starts in a direction with very low $h(n)$ values but later encounters high-cost obstacles or winding detours, GBFS will still follow it blindly because it does not track the cost already spent ($g(n)$).
* **Admissibility & Consistency:** For algorithms that guarantee the absolute shortest path (like $A^*$), the heuristic must be **admissible** (it must never overestimate the true remaining cost to the goal). GBFS, however, does not require strict admissibility to function, though poor heuristics will degrade its search efficiency.

---