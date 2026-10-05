# AI Lab – 3rd Semester

This repository contains implementations of fundamental Artificial Intelligence search, optimization, game-playing, and constraint-solving algorithms using Python.

## Algorithms Covered

* Beam Search
* Best First Search
* Breadth First Search (BFS)
* Depth First Search (DFS)
* Hill Climbing
* Iterative Deepening Search (IDS)
* Minimax with Alpha-Beta Pruning
* N-Queen Problem
* Uniform Cost Search (UCS)

## Algorithmic Flow

Most search algorithms in this repository follow a common problem-solving flow:

1. Define the problem or state space.
2. Represent states and possible transitions.
3. Select an appropriate search or optimization strategy.
4. Explore candidate states according to the algorithm.
5. Track visited states or relevant information when required.
6. Continue until the goal state is reached or the search space is exhausted.
7. Return or display the resulting path, solution, or decision.

The main difference between the algorithms is how they select the next state to explore.

## Search Algorithms

### Breadth First Search

BFS explores nodes level by level. It generally uses a queue and is useful when solutions are expected at shallow depths.

### Depth First Search

DFS explores one branch as deeply as possible before backtracking. The implementation uses a stack-based traversal and maintains visited nodes to avoid unnecessary repeated exploration.

### Best First Search

Best First Search selects the next state based on an evaluation or heuristic value, allowing the search to focus on promising states.

### Uniform Cost Search

UCS expands the node with the lowest accumulated path cost. It is useful when different paths have different costs.

### Iterative Deepening Search

IDS repeatedly performs depth-limited searches with increasing depth limits. It combines the depth-bounded behavior of DFS with the systematic depth exploration of BFS.

### Beam Search

Beam Search limits the number of candidate states retained at each level. This reduces the search space and can make the search more efficient when the complete search space is large.

## Optimization and Game Algorithms

### Hill Climbing

Hill Climbing is a local search technique that repeatedly moves toward a better neighbouring state according to an evaluation function. It is useful for optimization problems but can be affected by local optima.

### Minimax with Alpha-Beta Pruning

Minimax is used for decision-making in two-player games. It explores possible game states and selects moves assuming optimal play from both players.

Alpha-Beta Pruning improves Minimax by eliminating branches that cannot influence the final decision. This reduces unnecessary computation while preserving the result of the Minimax search.

## Constraint-Solving

### N-Queen Problem

The N-Queen problem places N queens on an N×N chessboard so that no two queens attack each other. It demonstrates state-space search and constraint satisfaction.

## Implementation Approach

The implementations are organized into separate directories according to the algorithm. Each directory contains the Python implementation and related code for that algorithm.

The programs generally follow this structure:

```text
Input / Initial State
        ↓
Problem Representation
        ↓
Search / Optimization Strategy
        ↓
State Exploration
        ↓
Goal / Solution Check
        ↓
Result / Traversal / Decision
```

## AI Engineering Relevance

These algorithms form the foundation of many Artificial Intelligence systems.

* Search algorithms are used for path finding and state-space exploration.
* Heuristic search helps prioritize promising states.
* Optimization algorithms can be used to find better solutions in large search spaces.
* Minimax and Alpha-Beta Pruning are fundamental techniques for game-playing AI.
* Constraint-solving techniques are useful for scheduling, planning, and configuration problems.

Understanding these algorithms helps in designing AI systems that can explore possible solutions, make decisions, and solve structured problems efficiently.

## Technology

* Python
* Artificial Intelligence
* Search Algorithms
* Heuristic Search
* Optimization
* Game-Playing Algorithms
* Constraint Satisfaction

## Repository Structure

```text
AI-LAB-3RD-SEM/
├── BeamSearch/
├── BestFirstSearch/
├── BreadthFirstSearch/
├── DepthFirstSearch/
├── HillClimbing/
├── IterativeDeepeningSearch/
├── MinMaxAlphaBetaSearch/
├── N-QueenProblem/
└── UniformCostSearch/
```

## Purpose

This repository is intended for learning and practicing fundamental Artificial Intelligence algorithms and understanding how different strategies explore states, optimize solutions, and make decisions.
