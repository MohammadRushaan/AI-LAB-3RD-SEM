def uniform_cost_search(graph, start, goal):
    # Priority queue storing tuples: (cumulative_cost, current_node, path)
    queue = [(0, start, [start])]
    visited = {}
    intermediate_paths = []

    print("\n--- Intermediate Paths Explored ---")
    step = 1

    while queue:
        # Sort queue descending by cost so pop() removes the lowest cost in O(1)
        queue.sort(key=lambda item: item[0], reverse=True)
        cost, current_node, path = queue.pop()

        # Record and display all intermediate paths explored
        intermediate_paths.append((path, cost))
        print(f"Step {step}: Path: {' -> '.join(path)} | Cumulative Cost: {cost}")
        step += 1

        # Goal test at expansion time
        if current_node == goal:
            return path, cost, intermediate_paths

        # Skip already evaluated paths with lower or equal cost
        if current_node in visited and visited[current_node] <= cost:
            continue
        visited[current_node] = cost

        # Expand neighboring nodes
        for neighbor, weight in graph.get(current_node, []):
            new_cost = cost + weight
            if neighbor not in visited or new_cost < visited[neighbor]:
                queue.append((new_cost, neighbor, path + [neighbor]))

    return None, float("inf"), intermediate_paths


def main():
    # 1. Take user input graph / tree
    graph = {}
    num_edges = int(input("Enter total number of edges: "))
    print("Enter each edge in format (source destination weight):")

    for _ in range(num_edges):
        u, v, w = input().strip().split()
        weight = float(w)
        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, [])  # Ensure destination node is initialized

    # 2. User input source node and goal node
    source = input("\nEnter Source Node: ").strip()
    goal = input("Enter Goal Node: ").strip()

    # Run UCS algorithm
    best_path, min_cost, all_intermediates = uniform_cost_search(
        graph, source, goal
    )

    # 3. Summary of all intermediate paths
    print("\n--- Summary of All Intermediate Paths ---")
    for idx, (path, cost) in enumerate(all_intermediates, 1):
        print(f"{idx}. {' -> '.join(path)} (Cost: {cost})")

    # 4. Show least cost path
    print("\n--- Result: Least Cost Path ---")
    if best_path:
        print(f"Optimal Path : {' -> '.join(best_path)}")
        print(f"Total Cost   : {min_cost}")
    else:
        print("No valid path exists between source and goal.")


main()