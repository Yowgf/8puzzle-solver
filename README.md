# 8-puzzle AI Solver

A solver for the 8-puzzle problem based on different Artificial Intelligence
space search algorithms.

# Usage

```shell
./solve <algoritm> <puzzle-entries> [PRINT] [-log-level=<log-level>]
                                  [PRINT_STATISTICS]
```

Available algorithms:

- **B** - Breadth-first search
- **I** - Iterative deepening
- **U** - Uniform cost search (Dijkstra)
- **A** - A* search

# Example

```shell
./solve B 1 2 3 4 5 6 7 0 8 PRINT -log-level=INFO
```
