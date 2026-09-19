## The Real-World Analogy: Climbing in Dense Fog
Imagine you are hiking up a mountain range covered in thick, blinding fog. You cannot see the summit or the surrounding peaks; you can only see the ground directly under your boots.

* The Goal: Reach the highest possible point.

* The Action: You extend your left foot by one step to test the elevation, then your right foot by one step. If the right step is higher than where you are standing, you step to the right.

* The Termination: You repeat this process until both your left and right steps lead downward. Because you can no longer step higher, you conclude you have reached a peak and stop.

## Key Concepts & Core Logic
Local Search Heuristic: The algorithm focuses entirely on improving the current state by exploring immediate neighbors rather than mapping the entire search space.

Greedy Decision Making: At every cycle, it picks the neighbor that provides the maximum immediate elevation gain.

No Backtracking / Memoryless: The algorithm never looks back or stores past paths; it only cares about where it is right now and where it can move next.

The Local Optima Dilemma: Because the search stops as soon as immediate neighbors are lower, the climber often settles on a smaller local peak rather than finding the highest peak (global maximum) on the entire landscape.

## Algorithmic Mechanics:
1. State Evaluation: The objective function $f(x)$ serves as the height meter.
2. Neighbor Generation: Using a fixed step size $\Delta x$, the search defines two candidate neighbors:   
    $x_{\text{left}} = x - \Delta x$   
    $x_{\text{right}} = x + \Delta x$   
3. Neighbor Evaluation: Both candidates are evaluated: $f(x_{\text{left}})$ and $f(x_{\text{right}})$.   
4. Transition Criterion:
    If $\max(f(x_{\text{left}}), f(x_{\text{right}})) > f(x)$, set $x \leftarrow \arg\max(f(x_{\text{left}}), f(x_{\text{right}}))$ and repeat.   
    If $\max(f(x_{\text{left}}), f(x_{\text{right}})) \le f(x)$, terminate.

## Matplotlib Explanation:

``` python
# 1. Sets the dimensions of the plotting window (width = 9 inches, height = 4.5 inches)
plt.figure(figsize=(9, 4.5))

# 2. Draws the smooth blue background wave by connecting all 1,001 points (curve_x, curve_y)
plt.plot(curve_x, curve_y, color="blue", label="f(x)")

# 3. Draws the search trajectory: 'o--' puts circular dots at every recorded step and connects them with dashed orange lines
plt.plot(path_x, path_y, "o--", color="orange", label="Climbing Steps")

# 4. Places a single green dot at the very first position (index 0) with a larger marker size (s=90)
plt.scatter(path_x[0], path_y[0], color="green", s=90, label="Start")

# 5. Places a single red star marker (marker="*") at the final stopping point (s=120)
plt.scatter(current_x, f(current_x), color="red", marker="*", s=120, label="Peak Found")

# 6. Adds the horizontal axis label
plt.xlabel("x")

# 7. Adds the vertical axis label
plt.ylabel("f(x)")

# 8. Displays the legend box showing which color/symbol corresponds to which label
plt.legend()

# 9. Displays light background grid lines to make reading coordinates easier
plt.grid(True)

# 10. Renders and opens the window displaying the complete graph
plt.show()

```
## How to Prevent Getting Trapped (Standard AI Mitigations):
1. Random-Restart Hill Climbing:
    Run the algorithm multiple times (e.g., 20 runs), each time picking a random starting $x$ within the domain.
    Save the peak found by each run.
    The highest peak among all runs will almost certainly be the true global maximum.
2. Simulated Annealing:
    Allows the algorithm to occasionally take downward/worse steps with a certain probability (controlled by a decreasing "temperature" parameter).
    This gives the agent the ability to cross valleys and escape local traps early in the search.
3. Stochastic / Variable Step Hill Climbing:
    Introduce randomized jumps or dynamically expand the step size when the algorithm detects it is stuck.