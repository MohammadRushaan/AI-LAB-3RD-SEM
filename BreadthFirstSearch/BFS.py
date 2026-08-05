from collections import deque

def bfs(graph, start_node):
    # Set to keep track of visited nodes (avoids infinite loops in cycles)
    visited = set()
    
    # Double-ended queue for O(1) pops from the left
    queue = deque([start_node])
    
    # Mark the initial node as visited
    visited.add(start_node)
    
    traversal_order = []
    
    while queue:
        # Pop the node that was added earliest
        current = queue.popleft()
        traversal_order.append(current)
        
        # Explore all adjacent unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order


# --- Example Usage ---
# Graph representation as an adjacency list
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

result = bfs(graph, 'A')
print("BFS Traversal Order:", result)
# Output: ['A', 'B', 'C', 'D', 'E', 'F']