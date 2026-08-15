# Priority Queue & Uniform Cost Search (UCS)

A **Priority Queue (PQ)** is an abstract data type where each element has an associated numerical priority, and elements are served based on their priority rather than their arrival order (unlike a standard FIFO queue). In most search algorithms, a **Min-Priority Queue** is used, where the element with the lowest numerical value is dequeued first.

---

## 1. Core Mechanics of a Priority Queue

A priority queue maintains a dynamically ordered collection of elements supporting four primary operations:

* **Insert (`push`)**: Add an element with an assigned priority.
* **Extract-Min (`pop`)**: Remove and return the element with the lowest priority value.
* **Peek (`top`)**: Inspect the minimum element without removing it.
* **Decrease-Key**: Lower the priority value of an existing element (critical for pathfinding and graph algorithms).

### Complexity Comparison

| Implementation | Insert | Extract-Min | Decrease-Key | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Unsorted Array / List** | $O(1)$ | $O(V)$ | $O(1)$ | $O(V)$ |
| **Binary Heap** | $O(\log V)$ | $O(\log V)$ | $O(\log V)$ | $O(V)$ |
| **Fibonacci Heap** | $O(1)$ amortized | $O(\log V)$ amortized | $O(1)$ amortized | $O(V)$ |

> **Note:** Binary heaps are the standard implementation choice in practice due to low memory overhead and predictable cache performance.

---

## 2. Uniform Cost Search (UCS)

**Uniform Cost Search** is an uninformed graph search algorithm that finds the lowest-cost path from a start node to a goal node in a weighted graph with non-negative edge costs $c(u, v) \ge 0$.

* It calculates the cumulative path cost $g(n)$ from the start node to current node $n$.
* It represents Dijkstra's algorithm generalized to implicit search spaces where the state graph is generated dynamically.
* It guarantees **optimality** and **completeness** provided step costs are strictly positive ($\epsilon > 0$).

---

## 3. How Priority Queues Drive UCS

The relationship between UCS and a Priority Queue is foundational: **the priority queue serves as UCS's frontier (open set), prioritizing nodes by cumulative path cost $g(n)$.**

```
                  +-------------------------------+
                  | Min-Priority Queue (Frontier) |
                  |   Elements keyed by g(n)      |
                  +-------------------------------+
                             |         ^
          Extract lowest g(n)|         | Push discovered
                             v         | neighbors: g(v) = g(u) + c(u,v)
                      +------------+   |
                      | Node Exp.  |---+
                      +------------+
```

### Key Principles

1. **Expansion Ordering**: By pulling from a Min-PQ, UCS always expands the node with the globally smallest cumulative cost $g(n)$ currently known.
2. **Concentric Cost Expansion**: UCS explores state space in order of increasing path cost $g(n)$, moving outward in cost-based contours rather than depth-based levels (as in BFS).
3. **Delayed Goal Test**: The goal condition is evaluated **only when a node is extracted from the PQ**, not when it is generated. This guarantees that no cheaper route to that goal node remains in the queue.

---

## 4. Handling Duplicate Paths in the Frontier

When a cheaper path to an already queued node is discovered, the algorithm must handle cost updates:

* **Explicit `Decrease-Key`**: Update the node's key in-place within the heap and restore the heap property ($O(\log V)$).
* **Lazy Deletion (Duplicate Insertion)**: Insert $(g_{\text{new}}(v), v)$ into the PQ without removing the older, higher-cost entry. When popping an element, check if a cheaper path to $v$ has already been finalized in the closed set/visited table; if so, discard it ($O(1)$ amortized overhead, slightly higher memory).

---

## 5. Python Implementation

```python
import heapq

def uniform_cost_search(graph, start, goal):
    # Frontier elements: (cumulative_cost, node_id, path)
    frontier = [(0, start, [start])]
    visited = {}

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        # Goal test at expansion time
        if node == goal:
            return cost, path

        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if neighbor not in visited or new_cost < visited[neighbor]:
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return float("inf"), []
```

---

## 6. Key Properties & Theoretical Bounds

* **Time Complexity**: $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$, where $C^*$ is the optimal path cost, $\epsilon$ is the minimum action cost, and $b$ is the branching factor.
* **Space Complexity**: $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$ due to holding all frontier nodes in the Priority Queue.
* **Relationship to BFS and A\***: 
  * If all edge costs are identical, UCS behaves identically to **Breadth-First Search (FIFO queue)**.
  * If a heuristic $h(n)$ is added such that the priority key becomes $f(n) = g(n) + h(n)$, UCS transforms into **A\* Search**.