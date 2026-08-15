# Uniform Cost Search:

Uniform Cost Search (UCS) is an optimal, uninformed graph search algorithm that finds the path with the lowest cumulative cost between a start node and a destination. It explores paths in strict order of their total accumulated cost rather than the number of hops.

## Real-World Analogy: Toll-Road Navigation
Imagine driving across the country with a GPS set to find the cheapest route in total toll fees, ignoring distance or time:

* The Intersection Choice: At every toll booth, you write down every route branching out ahead alongside the total tolls paid so far.

* The Decision Rule: You never pick a road just because it looks close on the map. Instead, you always put the vehicle on the route with the lowest total toll ticket printed to date.

* Finding the Destination: If a direct highway to your destination costs $50 in tolls, but an alternate winding route through three smaller towns costs $10 + $5 + $15 = $30, UCS will explore the three small towns first. It only announces arrival when your destination is the absolute cheapest option remaining on your dashboard.