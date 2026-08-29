def get_user_inputs():
    print("")

    num_edges = int(input("Enter total number of directed edges: ").strip())
    graph = {}

    print("\nEEnter each edge as two space-separated node:")
    for _ in range(num_edges):
        u, v = input().strip().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    print("\nEnter heuristic values for each node:")
    heuristics = {}
    for node in sorted(graph.keys()):
        hval = float(input(f"  Enter h({node}): ").strip())
        heuristics[node] = hval

    start_node = input("\nEnter Source / Start Node: ").strip()
    goal_node = input("Enter Goal Node: ").strip()

    return graph, heuristics, start_node, goal_node


def best_first_search(graph, heuristics, start, goal):
    # open_list stores tuples of (heuristic_value, [traversal_path])
    open_list = [(heuristics[start], [start])]
    visited = set()
    step = 1

    while open_list:
        # Sort open list ascending by heuristic value h(n)
        open_list.sort(key=lambda item: item[0])

        # Pop the node with the lowest heuristic value (index 0)
        hval, current_path = open_list.pop(0)
        current_node = current_path[-1]

        print(f"\n[Step {step}] Visiting Node: '{current_node}' (h = {hval})")
        print(f"  Current Path   : {' -> '.join(current_path)}")
        step =step + 1

        if current_node == goal:
            print(f"\nGOAL '{goal}' REACHED ")
            return current_path

        # Explore unvisited neighbors
        if current_node not in visited:
            visited.add(current_node)
            discovered = []

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    new_path = current_path + [neighbor]
                    open_list.append((heuristics[neighbor], new_path))
                    discovered.append(f"{neighbor}(h={heuristics[neighbor]})")

            print(f"  Visited Set    : {visited}")
            print(f"  Added to Open  : {discovered if discovered else 'None (Dead end)'}")
            print(f"  Remaining Open : {[(cost, path[-1]) for cost, path in open_list]}")

    print(f"\nGOAL '{goal}' UNREACHABLE ")
    return None


def main():
    graph, heuristics, start, goal = get_user_inputs()
    final_path = best_first_search(graph, heuristics, start, goal)

    print("")
    if final_path:
        print(f"FINAL TRAVERSAL PATH: {' -> '.join(final_path)}")
    else:
        print("No valid path exists between start and goal.")
    
main()