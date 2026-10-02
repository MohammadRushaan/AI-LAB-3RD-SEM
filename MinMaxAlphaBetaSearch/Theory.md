## The Core Concept:

Minimax and Alpha-Beta Pruning are decision-making algorithms used in two-player, zero-sum, perfect-information games (such as Chess, Checkers, and Tic-Tac-Toe):
* Zero-Sum: One player's gain is the exact equivalent of the other player's loss ($Utility_{MAX} + Utility_{MIN} = 0$).
* Perfect Information: There is no hidden information or randomness (like dice rolls or hidden cards); both players see the entire board state.
* Two Adversaries:
    MAX: Tries to choose the move that leads to the highest possible utility score.
    MIN: Tries to force the game toward the lowest possible utility score (assuming the opponent plays rationally and optimally).

## Real-World Analogy
Imagine you are negotiating to buy an apartment:

* You (MAX) want to maximize your savings.
* The Seller (MIN) wants to minimize your savings by selling at the highest price.

Suppose you visit two apartment buildings:

1. Building A: After negotiating all options, the lowest final price you can get is $100,000. You lock this in as your backup guarantee.
2. Building B: You inspect the cheapest base unit, and the seller immediately starts at $120,000.

Do you need to waste hours looking at the penthouse or luxury upgrades in Building B? No. The seller (MIN) will only try to charge you $120,000 or even more. Because you already have a guaranteed option of $100,000 in Building A, you walk away from Building B immediately.

That early exit is Alpha-Beta Pruning.

## How the Algorithms Work & Core Logic:

The Minimax Principle: 
Minimax evaluates game states recursively via Depth-First Search (DFS):
* It descends to the leaf nodes (the game's end or a search depth limit) and reads the terminal utility scores.
* It passes values upward:
    At a MAX node, it picks the largest value among its children:$$\text{Value}(n) = \max_{c \in \text{Children}(n)} \text{Value}(c)$$
    At a MIN node, it assumes the opponent will pick the smallest value:$$\text{Value}(n) = \min_{c \in \text{Children}(n)} \text{Value}(c)$$

### The Alpha-Beta Improvement:

Standard Minimax checks every single branch, even branches that will never be chosen. Alpha-Beta maintains two running bounds:
* $\alpha$ (Alpha): The best (highest) value MAX has guaranteed so far along the current path. Initialized to $-\infty$.
* $\beta$ (Beta): The best (lowest) value MIN has guaranteed so far along the current path. Initialized to $+\infty$.

As the tree is traversed:
* At a MAX node: We update $\alpha = \max(\alpha, \text{child\_value})$. If $\alpha \ge \beta$, we stop evaluating remaining siblings (Beta Cutoff), because the MIN ancestor above will never let this branch happen.
* At a MIN node: We update $\beta = \min(\beta, \text{child\_value})$. If $\beta \le \alpha$, we stop evaluating remaining siblings (Alpha Cutoff), because the MAX ancestor above already found a superior option elsewhere.

## 4. Comparison

| Feature | Standard Minimax | Alpha-Beta Pruning |
| :--- | :--- | :--- |
| **Final Result** | Guaranteed optimal score | Identical optimal score |
| **Worst-Case Time** | $O(b^d)$ | $O(b^d)$ (poor move ordering) |
| **Best-Case Time** | $O(b^d)$ | $O(b^{d/2})$ (optimal move ordering) |
| **Search Depth** | Limited by exponential growth | Can search up to twice as deep in the same time |
| **Space Complexity** | $O(b \cdot d)$ (call stack) | $O(b \cdot d)$ (call stack) |

*(where $b$ is the branching factor and $d$ is the tree depth/ply)*

## Applications, Failsafes & Optimizations:

1. Applications: Chess engines, Checkers, Connect Four, Othello, and economic multi-agent bargaining models.

2. Move Ordering: Alpha-Beta is fastest when the best moves are evaluated first. Techniques like Iterative Deepening and the    Killer Move Heuristic are used to guess the best moves early, cutting runtime down to $O(b^{d/2})$.

3. Horizon Effect & Quiescence Search: Fixed depth cuts can cause a program to overlook an immediate counter-attack right past the search boundary. Quiescence search extends exploration exclusively for captures or violent moves until the board state stabilizes.