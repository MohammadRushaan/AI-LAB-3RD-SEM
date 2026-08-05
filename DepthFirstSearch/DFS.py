graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # 1. Mark current node as visited
    visited.add(node)
    print(node, end=" ")

    # 2. Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

print("Recursive DFS Traversal:")
dfs_recursive(graph, 'A')