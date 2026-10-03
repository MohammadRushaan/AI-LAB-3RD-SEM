# Counters and list to record visited states and pruned structures
minimax_visited = 0
alphabeta_visited = 0
pruned_list = []

def input_and_build_tree():
    
    TreeDepth = int(input("Enter tree depth (must be > 3): "))
    while TreeDepth <= 3:
        print("Tree Depth must be greater than 3!")
        TreeDepth = int(input("Enter tree depth : "))

    branching = int(input("Enter branching factor: "))

    total_leaves = branching ** TreeDepth
    print("Enter", total_leaves, "leaf values separated by spaces:")

    text_values = input().split()
    while len(text_values) != total_leaves:
        print("You must enter exactly", total_leaves, "numbers. Try again:")
        text_values = input().split()

    leaf_values = []
    for item in text_values:
        leaf_values.append(int(item))

    # Build Tree
    def build(current_depth, node_index, is_max):
        # Base case: reached leaf depth, return integer value
        if current_depth == TreeDepth:
            return leaf_values.pop(0)

        node_name = "Node_D" + str(current_depth) + "_" + str(node_index)

        children = []
        for i in range(branching):
            child = build(current_depth + 1, node_index * branching + i, not is_max)
            children.append(child)

        return {
            "name": node_name,
            "is_max": is_max,
            "children": children
        }
    return build(0, 0, True)

def minmax(node):
    global minimax_visited
    minimax_visited = minimax_visited + 1

    # Base case: if it is an integer, it is a leaf
    if type(node) is int:
        return node

    if node["is_max"] is True:
        best = -9999
        for child in node["children"]:
            val = minmax(child)
            if val > best:
                best = val
        return best
    else:  # MIN node
        best = 9999
        for child in node["children"]:
            val = minmax(child)
            if val < best:
                best = val
        return best

def alphabeta(node, alpha, beta):
    global alphabeta_visited
    alphabeta_visited = alphabeta_visited + 1

    # Base case: leaf reached
    if type(node) is int:
        return node

    parent_name = node["name"]
    children = node["children"]

    if node["is_max"] is True:
        best = -9999
        for i in range(len(children)):
            child = children[i]
            val = alphabeta(child, alpha, beta)

            if val > best:
                best = val
            if best > alpha:
                alpha = best

            # Beta cutoff (at MAX node)
            if beta <= alpha:
                
                for unvisited in children[i + 1:]:
                    pruned_list.append({
                        "node": unvisited,
                        "parent": parent_name,
                        "reason": "Beta Cutoff (at MAX)"
                    })
                break
        return best

    else:  # MIN node
        best = 9999
        for i in range(len(children)):
            child = children[i]
            val = alphabeta(child, alpha, beta)

            if val < best:
                best = val
            if best < beta:
                beta = best

            # Alpha cutoff (at MIN node)
            if beta <= alpha:
                
                for unvisited in children[i + 1:]:
                    pruned_list.append({
                        "node": unvisited,
                        "parent": parent_name,
                        "reason": "Alpha Cutoff (at MIN)"
                    })
                break
        return best

def display(tree, mm_result, ab_result):
    
    def printTree(node, depth):
        space = "    " * depth
        if type(node) is dict:
            role = "MIN"
            if node["is_max"] is True:
                role = "MAX"
            print(space + "|-- [" + node["name"] + "] (" + role + ")")
            for child in node["children"]:
                printTree(child, depth + 1)
        else:
            print(space + "\\-- Terminal Leaf = " + str(node))

    print()
    print("1. SEARCH TREE STRUCTURE ")
    print()
    printTree(tree, 0)

    
    print()
    print("2. FINAL VALUES")
    print()
    print("Standard Minimax Root Result :", mm_result)
    print("Alpha-Beta Root Result       :", ab_result)

    
    print()
    print("3. PRUNED SUBTREES & TERMINAL NODES ")
    print()
    if len(pruned_list) > 0:
        cut_number = 1
        for item in pruned_list:
            pruned_item = item["node"]
            parent_name = item["parent"]
            reason = item["reason"]

            if type(pruned_item) is int:
                print(f"\n[Cut #{cut_number}] Terminal Leaf Pruned under [{parent_name}]")
                print("  Reason  :", reason)
                print("  Leaf    : Terminal Leaf Utility =", pruned_item)
            else:
                print(f"\n[Cut #{cut_number}] Entire Subtree Pruned under [{parent_name}]")
                print("  Reason  :", reason)
                print("  Subtree Structure & Skipped Leaves:")
                printTree(pruned_item, depth=1)

            cut_number = cut_number + 1
    else:
        print(" No nodes or subtrees were pruned.")

    print()
    print("4. COMPARISON: MINIMAX vs ALPHA-BETA")
    print()
    nodes_saved = minimax_visited - alphabeta_visited
    percent = (nodes_saved / minimax_visited) * 100

    print("Nodes explored by Minimax    :", minimax_visited)
    print("Nodes explored by Alpha-Beta :", alphabeta_visited)
    print("Total nodes skipped (pruned) :", nodes_saved)
    print("Search reduction percentage  : " + str(round(percent, 2)) + "%")

def main():
    tree = input_and_build_tree()
    mm_res = minmax(tree)
    ab_res = alphabeta(tree, -9999, 9999)
    display(tree, mm_res, ab_res)

main()