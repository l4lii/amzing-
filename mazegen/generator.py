import random
from collections import deque
WALL_BITS: dict[str, int] = {"N": 1, "E": 2, "S": 4, "W": 8}
WALL_OPPOSITE: dict[str, str] = {"N": "S", "E": "W", "S": "N", "W": "E"}
MOVES: dict[str, tuple[int, int]] = {
    "N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)
}


def create_closed_grid(width: int, height: int) -> list[list[int]]:
    """the function takes 2 parameters and creates a grid from
        that and return the list of ints that makes the grid"""
    return [[15 for _ in range(width)] for _ in range(height)]


def open_wall(grid: list[list[int]], x: int, y: int, direction: str) -> None:
    """Open the wall between a cell and its neighbour"""
    dx, dy = MOVES[direction]
    nx = x + dx
    ny = y + dy
    grid[y][x] &= ~WALL_BITS[direction]
    opposite = WALL_OPPOSITE[direction]
    grid[ny][nx] &= ~WALL_BITS[opposite]


def carve_maze(grid:list[list[int]], width: int, height: int, rng) -> None:
    visited: list[list[bool]] = [[False for _ in range(width)] for _ in range(height)]
    visited[0][0] = True
    stack: list[tuple[int, int]] = [(0, 0)]
    while stack:
        x, y = stack[-1]
        neighbours: list[tuple[str, int, int]] = []
        for direction in MOVES:
            dx, dy = MOVES[direction]
            nx = x + dx
            ny = y + dy
            if (0 <= nx < width) and (0 <= ny < height) and not visited[ny][nx]:
                neighbours.append((direction, nx, ny))
        if neighbours:
            direction, nx, ny = rng.choice(neighbours)
            open_wall(grid, x, y, direction)
            visited[ny][nx] = True
            stack.append((nx, ny))
        else:
            stack.pop()


def find_path(grid, entry: tuple[int, int], exit_: tuple[int, int]) -> list[str]:
    queue = deque([entry])
    came_from: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}
    height: int = len(grid)
    width: int = len(grid[0])
    while queue:
        x, y = queue.popleft()
        if (x, y) == exit_:
            break
        for direction in MOVES:
            dx, dy = MOVES[direction]
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < width
                and 0 <= ny < height
                and not grid[y][x] & WALL_BITS[direction]
                and (nx, ny) not in came_from
            ):
                came_from[(nx, ny)] = ((x, y), direction)
                queue.append((nx,ny))
    path: list[str] = []
    current: tuple[int, int] = exit_
    while current != entry:
        previous, direction = came_from[current]
        path.append(direction)
        current = previous
    path.reverse()
    return path
