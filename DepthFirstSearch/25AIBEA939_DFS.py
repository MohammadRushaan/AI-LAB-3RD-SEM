
def input_graph():
    # Takes user input to construct an adjacency list representation of a graph.

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


def dfs_traversal(graph, start_node):
    # Performs DFS using an explicit Stack data structure showing intermediate steps.
    # Iterative approach

    print(f"  DEPTH-FIRST SEARCH (DFS) FROM '{start_node}'  ")
    
    visited = []
    stack = [start_node]
    
    step = 1
    while stack:
        print(f"\n--- Step {step} ---")
        print(f"Stack before pop : {stack}")
        
        # Pop top element from stack
        current = stack.pop()
        
        if current not in visited:
            visited.append(current)
            print(f"Visited Node     : '{current}'")
            
            # Push adjacent unvisited neighbors to stack (reversed for left-to-right order)
            pushed = []
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    pushed.append(neighbor)
                    
            print(f"Nodes Pushed     : {list(reversed(pushed)) if pushed else 'None'}")
            print(f"Stack after pop  : {stack}")
            print(f"Path so far      : {' -> '.join(visited)}")
            step += 1
        else:
            print(f"Node '{current}' already visited. Skipping...")
            
    return visited

# Iterative approach requires stack but recursive approach doesn't


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
    
    # 3. Execute DFS
    dfs_path = dfs_traversal(graph, start_node)
    
    # 4. Final Traverse Paths
    print(f"DFS Traversal Path : {' -> '.join(dfs_path)}")

main()