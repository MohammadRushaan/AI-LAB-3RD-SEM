import math
import matplotlib.pyplot as plt

# Calcullate func value
def EqnVal(x):
    return math.sin(x) + 0.5 * math.sin(3 * x) + 0.2 * math.sin(7 * x)

# user inputs
xmin = float(input("Enter domain start: "))
xmax = float(input("Enter domain end: "))
current_x = float(input(f"Enter initial starting x [{xmin} to {xmax}]: "))
step_size = float(input("Enter step size: "))  

max_iter = 1000 # Prevent infinte loop  at platues if stuck

# Store the path taken  
path_x = [current_x]
path_y = [EqnVal(current_x)]

#  Hill Climbing Search 
for i in range(max_iter):
    # neighbors   
    left = max(xmin, current_x - step_size)  
    right = min(xmax, current_x + step_size)  
    
    # neighbor with higher value  
    if EqnVal(right) > EqnVal(left):
        best_neighbor = right
    else:
        best_neighbor = left
    
    # Move if the best neighbor improves the function value  
    if EqnVal(best_neighbor) > EqnVal(current_x):  
        current_x = best_neighbor
        path_x.append(current_x)
        path_y.append(EqnVal(current_x))
    else:
        break  # Peak reached  

print(f"\nFinal Peak Found: x = {current_x:.2f}, EqnVal(x) = {EqnVal(current_x):.2f}")
print(f"Total Steps Taken: {len(path_x) - 1}")

# points for plotting 
curve_x = []
curve_y = []

steps = 1000
dx = (xmax - xmin) / steps

curve_x = []
curve_y = []
for i in range(steps + 1):
    val = xmin + i * dx
    curve_x.append(val)
    curve_y.append(EqnVal(val))

# Plotting with Matplotlib  
plt.figure(figsize=(9, 4.5))
plt.plot(curve_x, curve_y, color="blue", label="EqnVal(x)")  
plt.plot(path_x, path_y, "o--", color="orange", label="Climbing Steps")  
plt.scatter(path_x[0], path_y[0], color="green", s=90, label=f"Start ({path_x[0]:.2f})")
plt.scatter(current_x, EqnVal(current_x), color="red", marker="*", s=120, label=f"Peak ({current_x:.2f})")

plt.title("Hill Climbing with Custom Domain and Step Size")
plt.xlabel("x")
plt.ylabel("EqnVal(x)")
plt.legend()
plt.grid(True)
plt.show()  