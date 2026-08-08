from collections import deque

def input_graph():
    #Takes user input to construct an adjacency list representation of a graph.
    
    graph = {}
    print("--- Graph Input ---")
    num_edges = int(input("Enter total number of edges: "))
    
    print("\nEnter each edge as two space-separated nodes (e.g., 'A B'):")
    for i in range(1, num_edges + 1):
        u, v = input(f"Edge {i}: ").strip().split()
        
        # Initialize nodes if not present
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
            
        # Add undirected edge connections
        graph[u].append(v)
        graph[v].append(u)
        
    return graph


def bfs_traversal(graph, start_node):
    """Performs BFS using an explicit Queue data structure showing intermediate steps."""
    print("\n==========================================")
    print(f" BREADTH-FIRST SEARCH (BFS) FROM '{start_node}' ")
    print("==========================================")
    
    visited = []
    queue = deque([start_node])
    queued_set = {start_node}
    
    step = 1
    while queue:
        print(f"\n--- Step {step} ---")
        print(f"Queue before pop : {list(queue)}")
        
        # Dequeue front element
        current = queue.popleft()
        visited.append(current)
        print(f"Visited Node     : '{current}'")
        
        # Add unvisited adjacent nodes to queue
        pushed = []
        for neighbor in graph.get(current, []):
            if neighbor not in visited and neighbor not in queued_set:
                queue.append(neighbor)
                queued_set.add(neighbor)
                pushed.append(neighbor)
                
        print(f"Nodes Enqueued   : {pushed if pushed else 'None'}")
        print(f"Queue after pop  : {list(queue)}")
        print(f"Path so far      : {' -> '.join(visited)}")
        step += 1
        
    return visited


def main():
    # 1. Get graph input
    graph = input_graph()
    
    # Display graph structure
    print("\nAdjacency List:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")
        
    # 2. Get source node input
    print("\n------------------------------------------")
    start_node = input("Enter the source node: ").strip()
    
    if start_node not in graph:
        print(f"Error: Node '{start_node}' does not exist in the graph.")
        return

    # 3. Execute BFS
    bfs_path = bfs_traversal(graph, start_node)
    
    # 4. Print Outcome
    print(f"BFS Traversal Path : {' -> '.join(bfs_path)}")
    
main()