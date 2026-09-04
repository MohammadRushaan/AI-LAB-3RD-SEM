def beam_search(graph, heuristics, start, goal, beam_width):
    print("")
    print(f"         BEAM SEARCH (Width = {beam_width})         ")

    # Stores tuples: (heuristic, current_node, path)
    beam = [(heuristics.get(start, float("inf")), start, [start])]
    visited = {start}
    level = 1

    while beam:
        print(f"\n--- Level {level} ---")
        candidates = []

        # Check if any path in the current beam reached the goal
        for hval, current, path in beam:
            print(f"Expanding: '{current}' (h={hval}) | Path: {' -> '.join(path)}")
            if current == goal:
                print(f"\nGoal node '{goal}' reached successfully")
                return path

            # Explore all unvisited successors
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    candidates.append(
                        (
                            heuristics.get(neighbor, float("inf")),
                            neighbor,
                            path + [neighbor],
                        )
                    )

        if not candidates:
            break

        # Sort all successors by heuristic value (ascending) and select top-k
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:beam_width]

        selected_nodes = []
        for item in beam:
            selected_nodes.append(item[1])

        print(f"Selected Beam Candidates for next step: {selected_nodes}")
        level = level + 1

    print(f"\nGoal node '{goal}' not reachable within beam constraints.")
    return None

def main():
    graph = {}
    heuristics = {}

    print()
    num_nodes = int(input("Enter number of nodes: "))

    for i in range(num_nodes):
        node = input("Enter node name: ").strip()
        hval = float(input(f"Enter heuristic value for node '{node}': "))
        heuristics[node] = hval
        graph[node] = []

    num_edges = int(input("\nEnter number of directed edges: "))
    print("Enter edges in format: <source> <destination>")
    for i in range(num_edges):
        u, v = input().split()
        graph[u].append(v)
        #graph[v].append(u)

    start = input("\nEnter source node: ").strip()
    goal = input("Enter goal node: ").strip()
    beam_width = int(input("Enter beam width (k): "))

    path = beam_search(graph, heuristics, start, goal, beam_width)

    print("")
    if path:
        print("Final Traversal Path:", " -> ".join(path))
    else:
        print("Final Traversal Path: No Path Found")
    print("")

main()