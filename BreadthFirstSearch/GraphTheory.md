# What is a Graph?

A Graph is a non-linear data structure designed to represent network connections between items.Unlike arrays or linked lists (which store data in a straight line) or trees (which store data in a strict top-down hierarchy), a graph can connect elements in any pattern imaginable, including cyclic loops.

### The Two Building Blocks:
Every graph consists of two main components:
Vertices (Nodes): The entities holding data. (e.g., people, web pages, cities).
Edges: The connections or links between nodes. (e.g., friendships, hyperlinks, roads).

Mathematically, a graph G is represented as a set of vertices V and edges E: G = (V, E).
---

### How a Graph Works (Core Concept):

Unlike linear data structures (Arrays, Linked Lists) or hierarchical structures (Trees, where nodes have strict parent-child relationships), a graph allows arbitrary relationships. Any vertex can connect to any number of other vertices.  
Structural Variations:
Directed (Digraph): Edges have an explicit direction (u to v).  Example: Following someone on Twitter/X (A follows B does not imply B follows A).  
Undirected: Edges are bidirectional (u to v or v to u).  Example: A Facebook friendship (mutual connection).  
Weighted: Each edge carries a numerical value or cost (e.g., distance, latency, capacity).  
Unweighted: Edges have uniform cost (default cost = 1)

---
### Graph Memory Representations:

To store and query graphs efficiently in memory, two major representations are used:
A. Adjacency Matrix: A 2D matrix M of size V X V where M[i][j] = 1 (or weight) indicates an edge from node i to node j.  
Space Complexity: O(V^2) 
Edge Lookup O(1): Instant check if an edge exists between i and j.
Best used for: Dense graphs.

B. Adjacency List: An array or hash map where each index i stores a list of adjacent neighbors.
Space Complexity: O(V + E)
Neighbor Iteration O(Degree): Quick traversal of connected nodes.
Best used for: Sparse graphs .

---

### What is Graph Traversal?

Graph Traversal means systematically visiting every node in a graph to process information, search for a target value, or discover network patterns.

Why standard tree traversal isn't enough for graphs:
No Root Node: A graph doesn't have a guaranteed top/root node. You can start traversal from any vertex.

Cycles (Infinite Loops): Graphs can contain loops. Node A might lead to Node B, which leads back to Node A.

Crucial Rule of Graph Traversal: You must keep track of visited nodes (usually using a set or boolean array). Without a visited tracker, a traversal algorithm will loop infinitely!

---
# Summary of Common Graph Algorithms

| Traversal / Algorithm | Data Structure | Best Use Case | Time Complexity |
| :--- | :--- | :--- | :--- |
| **BFS** | Queue | Shortest path in unweighted graph | $O(V + E)$ |
| **DFS** | Stack / Recursion | Pathfinding, cycle detection | $O(V + E)$ |
| **Topological Sort** | Queue + In-Degree Array | Task dependency ordering | $O(V + E)$ |
| **Dijkstra** | Priority Queue (Min-Heap) | Shortest path in weighted graph | $O((V + E) \log V)$ |

