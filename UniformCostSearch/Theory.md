# Uniform Cost Search:

Uniform Cost Search (UCS) is an optimal, uninformed graph search algorithm that finds the path with the lowest cumulative cost between a start node and a destination. It explores paths in strict order of their total accumulated cost rather than the number of hops.

## Real-World Analogy: Toll-Road Navigation
Imagine driving across the country with a GPS set to find the cheapest route in total toll fees, ignoring distance or time:

* The Intersection Choice: At every toll booth, you write down every route branching out ahead alongside the total tolls paid so far.

* The Decision Rule: You never pick a road just because it looks close on the map. Instead, you always put the vehicle on the route with the lowest total toll ticket printed to date.

* Finding the Destination: If a direct highway to your destination costs $50 in tolls, but an alternate winding route through three smaller towns costs $10 + $5 + $15 = $30, UCS will explore the three small towns first. It only announces arrival when your destination is the absolute cheapest option remaining on your dashboard.

---
## Core Logic:
    [Start Node]
            │
            ▼
    [Priority Queue] <─── Insert (Cumulative Cost, Node, Path)
            │
            ├─► Pop element with lowest cost: (g(n), n, path)
            │
    [Is n the Goal?] ──YES──► Return Path & Cost (Optimal Solution Found)
            │
            NO
            │
    [Has n been visited cheaper?] ──YES──► Discard (Prune)
            │
            NO
            ▼
   [Mark n as Visited]
            │
   [For each neighbor m of n] ──► Calculate new_cost = g(n) + edge_cost(n, m)
            │                     Push (new_cost, m, path + [m]) to Priority Queue
            ▼
   (Repeat until queue is empty or goal reached)

Cost Function g(n): Measures the exact path cost from the root/start node to the current node n.

Exploration Strategy: Implements a min-priority queue (min-heap) ordered by g(n).

Delayed Goal Test: The goal check occurs upon extraction (pop) from the priority queue, not during insertion (generation). Because edge costs are non-negative, extracting the goal guarantees that every other active path in the frontier has a cost 

Optimality & Completeness: Guaranteed to find the optimal path if all edge costs c >epsilon > 0.

Time and space complexity are $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$, where $C^*$ is the optimal path cost and $b$ is the branching factor.

---
### CODE:

```python

import heapq


def uniform_cost_search(graph, start, goal):
    # Min-priority queue stores: (cumulative_cost, current_node, path_list)
    frontier = [(0, start, [start])]

    # Tracks the minimal cost encountered for visited nodes
    visited = {}

    while frontier:
        # 1. Pop the path with the smallest accumulated cost
        cost, current_node, path = heapq.heappop(frontier)

        # 2. Goal test upon extraction
        if current_node == goal:
            return path, cost

        # 3. Prune if already expanded via an equal or cheaper path
        if current_node in visited and visited[current_node] <= cost:
            continue

        # 4. Mark node with its finalized minimum cost
        visited[current_node] = cost

        # 5. Expand neighbors
        for neighbor, edge_weight in graph.get(current_node, []):
            new_cost = cost + edge_weight
            if neighbor not in visited or new_cost < visited[neighbor]:
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return None, float("inf")

```
---
### Step-by-Step Code Flow:
Consider searching from S to G on this graph:
S -> A (cost 2), S -> B (cost 5)
A -> G (cost 10), A -> C (cost 1)
C -> G (cost 3)
B -> G (cost 4)

Initialization: 
* frontier = [(0, 'S', ['S'])]
* visited = {}

Iteration 1:
heappop yields (0, 'S', ['S']).
Not goal. Mark visited['S'] = 0.
Push neighbors: (2, 'A', ['S', 'A']) and (5, 'B', ['S', 'B']).

Iteration 2:
Smallest in heap is (2, 'A', ['S', 'A']). 
heappop extracts 'A'.
Not goal. Mark visited['A'] = 2.
Push neighbors:To C: 2 + 1 = 3 ---> (3, 'C', ['S', 'A', 'C'])
               To G: 2 + 10 = 12 ---> (12, 'G', ['S', 'A', 'G'])
               
Iteration 3:
Smallest in heap is (3, 'C', ['S', 'A', 'C']). 
heappop extracts 'C'.
Not goal. Mark visited['C'] = 3.
Push neighbor:To G: 3 + 3 = 6 ---> (6, 'G', ['S', 'A', 'C', 'G'])

Iteration 4:
Smallest in heap is (5, 'B', ['S', 'B']).
heappop extracts 'B'.
Not goal. Mark visited['B'] = 5.
Push neighbor:To G: 5 + 4 = 9 ---> (9, 'G', ['S', 'B', 'G'])

Iteration 5:
Smallest in heap is (6, 'G', ['S', 'A', 'C', 'G']).
heappop extracts 'G'.
Goal match triggers: returns path ['S', 'A', 'C', 'G'] with total cost 6. (Notice that the direct routes to G with costs 9 and 12 were bypassed).

---
## Applications & Use Cases:
* GPS Navigation & Toll Optimization: Computing routes where the primary constraint is not geographical distance, but variable metrics such as monetary toll cost, fuel burn, or road roughness.
* Network Packet Routing: Finding minimal-latency or lowest-congestion data paths across heterogeneous network links with dynamic bandwidth costs.
* Robotic Motion Planning: Guiding autonomous rovers across varied terrain (e.g., mud, paved roads, steep inclines) where each terrain type assigns a different movement penalty.
* Game Development & Pathfinding: Non-grid AI movement in strategy games where different terrain tiles have distinct movement stamina costs and no consistent heuristic is available.

Critical Failsafes & Failure Modes
1. Positive Step Cost Requirement ($\epsilon > 0$)The Risk: If edges have zero cost ($c = 0$) or negative cost ($c < 0$), UCS can enter infinite loops along zero/negative-cost cycles, continuously expanding without making forward progress.Failsafe: Validate all edge weights during graph ingestion ($\text{cost} > 0$). For graphs with negative edge weights, use the Bellman-Ford algorithm instead.
2. Goal-Testing on Expansion (Not Generation)The Risk: Testing whether a node is the goal upon adding it to the priority queue leads to suboptimal solutions, as a cheaper alternative path to that same goal might still be waiting in the queue.Failsafe: Always evaluate if current_node == goal immediately after extracting (popping) from the queue, guaranteeing that the popped cost is minimal.
3. State-Pruning with Closed/Visited SetsThe Risk: Graphs with cycles or redundant paths can cause exponential state space explosions or infinite loops if nodes are repeatedly re-expanded.Failsafe: Maintain a visited hash map storing the lowest known cost to each node:

```python
if current_node in visited and visited[current_node] <= cost:
    continue
visited[current_node] = cost

```
4. Tie-Breaking InconsistenciesThe Risk: If two paths share identical cumulative costs, standard tuple comparisons (cost, node, path) may crash if node objects are unhashable or non-comparable.Failsafe: Include an incrementing unique integer or timestamp counter in the tuple: (cost, count, node, path).

---