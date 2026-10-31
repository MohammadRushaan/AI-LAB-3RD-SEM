def input_graph():
   
    graph = {}
    
    num_edges = int(input("Enter total number of edges: "))
    
    print("\nEnter each edge as two space-separated nodes :")
    for i in range(1, num_edges + 1):
        u, v = input(f"Edge {i}: ").strip().split()
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
            
        graph[u].append(v)
        graph[v].append(u)
        
    return graph


def bfs_traversal(graph, start_node, goal_node):
    
    visited = []
    queue = [start_node]

    while queue:
        
        current = queue.pop(0)
        visited.append(current)

        if current == goal_node:
            break
            
        for neighbor in graph.get(current, []):
            if neighbor not in visited :
                queue.append(neighbor)
                
    return visited

def length(lis):
    count=0
    for i in lis:
        count=count+1
    return count

def main():
    
    graph = input_graph()

    start_node = input("Enter the source node: ").strip()
    
    if start_node not in graph:
        print(f"Error: Node '{start_node}' does not exist in the graph.")
        return

    shortest_path=0
    len=999
    goal_nodes = input(" Enter goal nodes seperated by space:").strip().split()
    for goal in goal_nodes:
        bfs_path = bfs_traversal(graph, start_node, goal)
        if len > length(bfs_path):
            len = length(bfs_path)
            shortest_path= bfs_path
        print(f"BFS Traversal Path : {bfs_path}")

    print("Shortest Path:", shortest_path)
    
main()