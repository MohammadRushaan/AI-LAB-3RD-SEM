# Lists and counters to track results
minimax_visited = 0
alphabeta_visited = 0
pruned_list = []


def input_and_build_tree():
    
    TreeDepth = int(input("Enter tree depth (must be > 3): "))
    while TreeDepth <= 3:
        print("must be greater than 3!")
        TreeDepth = int(input("Enter tree depth : "))

    branching = int(input("Enter branching factor : "))

    total_leaves = branching ** TreeDepth
    print("Enter", total_leaves, "leaf values separated by spaces:")
    
    text_values = input().split()
    while len(text_values) != total_leaves:
        print("You must enter exactly", total_leaves, "numbers. Try again:")
        text_values = input().split()

    leaf_values = []
    for item in text_values:
        leaf_values.append(int(item))

    
    def build(current_depth, is_max):
        # Base case: reached bottom depth, return the next leaf number
        if current_depth == TreeDepth:
            return leaf_values.pop(0)

        children = []
        for i in range(branching):
            # Alternate turn: if current is MAX, child is MIN (not is_max)
            child = build(current_depth + 1, not is_max)
            children.append(child)
        #dictionary 
        return {
            "is_max": is_max,
            "children": children
        }

    # Start tree at depth 0 with MAX as Root
    return build(0, True)


def minmax(node):
    global minimax_visited
    minimax_visited = minimax_visited + 1

    # Base case: if it is an integer, it is a leaf
    if type(node) is int:
        return node

    # MAX Player's turn
    if node["is_max"] is True:
        best = -9999
        for child in node["children"]:
            val = minmax(child)
            if val > best:
                best = val
        return best

    # MIN Player's turn
    else:
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

    children = node["children"]

    # MAX Player's turn
    if node["is_max"] is True:
        best = -9999
        for i in range(len(children)):
            child = children[i]
            val = alphabeta(child, alpha, beta)

            if val > best:
                best = val
            if best > alpha:
                alpha = best

            # Beta cutoff: Stop evaluating remaining children
            if beta <= alpha:
                for unvisited in children[i + 1:]:
                    pruned_list.append("Beta cutoff at MAX")
                break
        return best

    # MIN Player's turn
    else:
        best = 9999
        for i in range(len(children)):
            child = children[i]
            val = alphabeta(child, alpha, beta)

            if val < best:
                best = val
            if best < beta:
                beta = best

            # Alpha cutoff: Stop evaluating remaining children
            if beta <= alpha:
                for unvisited in children[i + 1:]:
                    pruned_list.append("Alpha cutoff at MIN")
                break
        return best


def display(tree, mm_result, ab_result):
    def show_tree(node, depth):
        space = "    " * depth
        if type(node) is dict:
            role = "MIN"
            if node["is_max"] is True:
                role = "MAX"
            print(space + "|-- " + role)
            for child in node["children"]:
                show_tree(child, depth + 1)
        else:
            print(space + "\\-- Leaf = " + str(node))

    print()
    print("SEARCH TREE STRUCTURE")
    print()
    show_tree(tree, 0)

    print()
    print("RESULTS")
    print()
    print("Minimax Root Value    :", mm_result)
    print("Alpha-Beta Root Value :", ab_result)

    print()
    print("PRUNING DETAILS")
    print()
    if len(pruned_list) > 0:
        for cut in pruned_list:
            print(" * Skipped branch due to:", cut)
    else:
        print(" No branches were pruned.")

    print()
    print("COMPARISON")
    print()
    saved = minimax_visited - alphabeta_visited
    percent = (saved / minimax_visited) * 100

    print("Minimax nodes checked    :", minimax_visited)
    print("Alpha-Beta nodes checked :", alphabeta_visited)
    print("Nodes saved (pruned)     :", saved)
    print("Efficiency improvement   :", round(percent, 2), "%")


def main():
    tree = input_and_build_tree()
    mm_res = minmax(tree)
    ab_res = alphabeta(tree, -9999, 9999)
    display(tree, mm_res, ab_res)

main()