# Travelling Salesman Problem (TSP)
- Find the shortest route to visit each node once https://en.wikipedia.org/wiki/Travelling_salesman_problem
- And more precisely the Travelling Purchaser: Find the shortest route for a given list of products to buy https://en.wikipedia.org/wiki/Traveling_purchaser_problem
We are in a symmetric Problem because it takes as much time to go from A to B than from B to A.

# Implementation of Nearest Neighbour algorithm (NN) - 25% longer than shortest
- create list of bars with id+coords, ex: 1 (3;5), 2 (0;4)...
- get first bar id, ex: 5
- get drinks list
- set bars drinks price
- for each drink
  - for each bar
    - get its distanceToBar N-1 and its price of drink N (absolute values)
  - define closestBar + cheapestBar
  - for each bar
    - set distanceRel(=closestBar.distance / barN.distanceToBar) and priceRel (relative values)
    - Px = distanceRel * priceRel
  - find bar with higher Px
