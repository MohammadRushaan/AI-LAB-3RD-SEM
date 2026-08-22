from collections import defaultdict

def dls(graph, current_node, goal_node, limit, path, visited_order):
    #Depth-Limited Search helper function using recursion.
    visited_order.append(current_node)
    path.append(current_node)

    # Base Case: Goal found
    if current_node == goal_node:
        return True

    # Base Case: Depth limit reached
    if limit <= 0:
        path.pop()
        return False

    # Recursive Case: Explore neighbors
    for neighbor in graph.get(current_node, []):
        if neighbor not in path:  # Avoid cycles in graphs
            if dls(graph, neighbor, goal_node, limit - 1, path, visited_order):
                return True

    path.pop()  # Backtrack
    return False


def iterative_deepening_search(graph, start, goal, max_depth=20):
    #Executes IDS from depth 0 up to max_depth, showing all intermediate steps.
    print(" ")
    print("STARTING ITERATIVE DEEPENING SEARCH")
    print(f"Source: {start} | Goal: {goal}")
    print(" ")

    for depth in range(max_depth + 1):
        path = []
        visited_order = []
        print(f"\n--- Depth Limit: {depth} ---")

        found = dls(graph, start, goal, depth, path, visited_order)

        print(f"Nodes visited in order: {' -> '.join(visited_order)}")

        if found:
            print(f"\n[+] Goal '{goal}' found at depth level {depth}!")
            print(f"[+] Final Traversal Path: {' -> '.join(path)}")
            return path

    print(f"\n[-] Goal '{goal}' could not be found within depth limit {max_depth}.")
    return None


def main():
    graph = defaultdict(list)

    print("=== GRAPH INPUT ===")
    num_edges = int(input("Enter total number of edges: "))

    print("Enter each edge as: <parent> <child> (e.g., A B)")
    for i in range(num_edges):
        u, v = input(f"Edge {i+1}: ").strip().split()
        graph[u].append(v)
        graph[v].append(u)

    source = input("\nEnter source node: ").strip()
    goal = input("Enter goal node: ").strip()
    max_threshold = int(
        input("Enter maximum search depth threshold (e.g., 5): ")
    )

    iterative_deepening_search(graph, source, goal, max_threshold)


main()