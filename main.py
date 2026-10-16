"""
Maze Solver using A* Search
SYNTECXHUB Project 1

Run:
    python main.py

No third-party packages are required.
"""

import heapq
import itertools

# 0 = open cell, 1 = wall
MAZE = [
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0],
]

START = (0, 0)
GOAL = (6, 6)


def heuristic(cell, goal):
    """Manhattan distance: suitable for four-direction movement."""
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def get_neighbors(cell, maze):
    """Return walkable up/down/left/right neighboring cells."""
    row, col = cell
    rows, cols = len(maze), len(maze[0])
    candidates = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]
    return [
        (r, c) for r, c in candidates
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0
    ]


def a_star(maze, start, goal):
    """
    Find the shortest path with A*.
    Returns (path, visited_order); path is [] if goal is unreachable.
    """
    rows, cols = len(maze), len(maze[0])
    for name, point in (("start", start), ("goal", goal)):
        r, c = point
        if not (0 <= r < rows and 0 <= c < cols):
            raise ValueError(f"{name.title()} position is outside the maze.")
        if maze[r][c] == 1:
            raise ValueError(f"{name.title()} position cannot be a wall.")

    counter = itertools.count()
    open_heap = [(heuristic(start, goal), 0, next(counter), start)]
    came_from = {}
    g_score = {start: 0}
    closed = set()
    visited_order = []

    while open_heap:
        _, current_cost, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        closed.add(current)
        visited_order.append(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, visited_order

        for neighbor in get_neighbors(current, maze):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(
                    open_heap,
                    (f_score, tentative_g, next(counter), neighbor)
                )

    return [], visited_order


def display_maze(maze, start, goal, path=None, visited=None):
    """Print the maze in the console with a legend."""
    path = set(path or [])
    visited = set(visited or [])
    for r, row in enumerate(maze):
        symbols = []
        for c, value in enumerate(row):
            cell = (r, c)
            if cell == start:
                symbol = "S"
            elif cell == goal:
                symbol = "G"
            elif value == 1:
                symbol = "#"
            elif cell in path:
                symbol = "*"
            elif cell in visited:
                symbol = "+"
            else:
                symbol = "."
            symbols.append(symbol)
        print(" ".join(symbols))
    print("Legend: S = Start, G = Goal, # = Wall, * = Shortest path, + = Explored, . = Open")


def main():
    print("=" * 46)
    print("        MAZE SOLVER USING A* SEARCH")
    print("=" * 46)
    print("\nOriginal maze:")
    display_maze(MAZE, START, GOAL)

    try:
        path, visited = a_star(MAZE, START, GOAL)
    except ValueError as error:
        print(f"\nInput error: {error}")
        return

    print("\nSearch result:")
    if path:
        display_maze(MAZE, START, GOAL, path, visited)
        print(f"\nPath found! Number of moves: {len(path) - 1}")
        print("Path coordinates (row, column):")
        print(" -> ".join(map(str, path)))
        print(f"Cells explored: {len(visited)}")
    else:
        print("No path exists between the start and goal.")
        print(f"Cells explored: {len(visited)}")


if __name__ == "__main__":
    main()
