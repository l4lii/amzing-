from mazegen import generator
from mazegen.generator import MazeGenerator
import random

if __name__ == "__main__":
    """
    grid1 = generator.create_closed_grid(8, 6)
    rng1 = random.Random(1)
    generator.carve_maze(grid1, 8, 6, rng1)
    for row in grid1:
        print("".join(f"{c:X}" for c in row))
    grid2 = generator.create_closed_grid(8, 6)
    rng2 = random.Random(1)
    generator.carve_maze(grid2, 8, 6, rng2)
    print("")
    for row in grid2:
        print("".join(f"{c:X}" for c in row))
    print("")
    if grid1 == grid2:
        print(True)
    else:
        print(False)

    grid = generator.create_closed_grid(8, 6)
    generator.carve_maze(grid, 8, 6, random.Random(1))
    print(generator.find_path(grid, (0, 0), (7, 5)))
    """
"""
if __name__ == "__main__":
    grid = generator.create_closed_grid(15, 11)
    blocked = generator.get_pattern_cells(15, 11)
    rng = random.Random(1)
    generator.carve_maze(grid, 15, 11, rng, blocked)
    for row in grid:
        print("".join(f"{c:X}" for c in row))
    print(len(generator.find_dead_ends(grid)))
"""
"""
grid = generator.create_closed_grid(15, 11)
blocked = generator.get_pattern_cells(15, 11)
rng = random.Random(1)
generator.carve_maze(grid, 15, 11, rng, blocked)
print(len(generator.find_dead_ends(grid)))
generator.braid_dead_ends(grid, blocked, rng)
print(len(generator.find_dead_ends(grid)))
print(generator.has_open_3x3(grid))
print(generator.find_dead_ends(grid))
print(grid[0][0], grid[0][14], grid[10][0], grid[10][14], grid[5][7])
print(generator.has_two_routes(grid, (0, 0), (14, 10)))
"""
gen = MazeGenerator(15, 11, (0, 0), (14, 10), perfect=False, seed=1)
print(gen.width, gen.height, gen.entry, gen.exit)
print(gen.grid)

for bad in [((3, 99), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (99, 3))]:
    try:
        MazeGenerator(15, 11, bad[0], bad[1])
    except ValueError as error:
        print("Errore:", error)