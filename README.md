# Maze Solver using A* Search

**SYNTECXHUB — Project 1**

## Overview
This project finds a shortest path through a grid maze using the A* search algorithm. The maze contains a start cell, a goal cell, open cells, and walls.

## Requirements
- Python 3.8 or later
- No external Python packages are needed

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

## Maze symbols
- `S` — start
- `G` — goal
- `#` — wall
- `*` — shortest path
- `+` — cells explored by the search
- `.` — open cell not on the displayed path

## How A* works
A* selects the next cell using:

`f(n) = g(n) + h(n)`

- `g(n)` is the cost from the start to the current cell.
- `h(n)` is the estimated remaining distance to the goal.
- This project uses Manhattan distance: `abs(row difference) + abs(column difference)`.
- Movement is allowed up, down, left, and right, with a cost of 1 per move.

With this heuristic and four-direction movement, A* finds a shortest path when one exists. If the goal cannot be reached, the program reports that no path exists.

## Main functions
- `heuristic()` — calculates Manhattan distance.
- `get_neighbors()` — returns valid adjacent open cells.
- `a_star()` — runs the A* algorithm and reconstructs the path.
- `display_maze()` — displays the maze and result in the terminal.
- `main()` — runs the demonstration.

## Test ideas
1. Run the default maze and check the shortest path.
2. Change a `0` in `MAZE` to `1` to add a wall.
3. Surround the goal with walls and check the unreachable-goal message.
4. Change `START` or `GOAL` to another open cell.

## GitHub submission
Create a repository named `Syntecxhub_Maze_Solver` (or follow the exact naming format specified by your internship coordinator), then upload `main.py` and `README.md`.

Suggested repository description:
`A Python implementation of the A* search algorithm to find a shortest path through a grid maze.`

Before submitting, run the program yourself and make sure you understand the algorithm and output. Follow the internship's official submission form and deadline.
