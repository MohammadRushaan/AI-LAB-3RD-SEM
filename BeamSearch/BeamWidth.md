**Beam Width ($k$)** is the fixed number of most promising candidate paths that the algorithm is allowed to retain at any single level during its search.

Instead of keeping track of every possible branch like Breadth-First Search (BFS), Beam Width acts as a strict filter that limits the memory footprint and computation time.


**1. How Beam Width is Implemented in the Code**

In the script, the beam width constraint is enforced using standard list sorting and slicing (`[:beam_width]`):

```python
# Step 1: Collect all valid child paths from the current level
candidates = []
for h_val, current, path in beam:
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            candidates.append((heuristics.get(neighbor, float("inf")), neighbor, path + [neighbor]))

# Step 2: Sort all newly discovered candidate paths by heuristic score (lowest h(n) first)
candidates.sort(key=lambda x: x[0])

# Step 3: Apply Beam Width (k) via Python slice
beam = candidates[:beam_width]

```

* `candidates.sort(key=lambda x: x[0])` orders all generated successor paths so that the node with the lowest heuristic value (closest to the goal) appears first.
* `beam = candidates[:beam_width]` keeps only the first $k$ elements and permanently discards the rest from memory.

**2. The Effect of Beam Width ($k$)**

The choice of $k$ directly controls the trade-off between **efficiency** (speed/memory) and **accuracy** (finding the optimal path).

* **When $k = 1$ (Greedy Best-First Search / Hill Climbing)**
* **Behavior:** At each level, the algorithm only picks the single best child node.
* **Memory/Time:** Minimal memory usage ($O(d)$), runs very fast.
* **Risk:** High chance of getting stuck in dead ends or local minima because it cannot explore alternative paths if its single choice is wrong.


* **When $1 < k < \infty$ (Standard Beam Search)**
* **Behavior:** Explores $k$ parallel paths simultaneously.
* **Memory/Time:** Controlled and predictable ($O(k \cdot d)$ space complexity).
* **Risk:** Significantly less prone to dead ends than $k=1$, but still not guaranteed to be complete or optimal if the true shortest path was pruned early on.


* **When $k = \infty$ (or $k \ge \text{branching factor}$)**
* **Behavior:** Degrades into standard Breadth-First Search (BFS).
* **Memory/Time:** Explores every valid path, causing memory to explode exponentially ($O(b^d)$).
* **Advantage:** Complete (guaranteed to find a path if one exists).


**Summary Comparison**

| Metric | Small Beam Width ($k = 1$ or $2$) | Moderate Beam Width ($k = 5$ to $10$) | Large / Infinite Beam Width ($k \rightarrow \infty$) |
| --- | --- | --- | --- |
| **Memory Usage** | Extremely Low | Low & Bounded | High (Exponential) |
| **Search Speed** | Very Fast | Fast | Slower on large graphs |
| **Path Quality** | Often suboptimal / prone to fail | Balanced / high success rate | Optimal / Complete |
| **Pruning Rate** | Aggressive | Moderate | None |