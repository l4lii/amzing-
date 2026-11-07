from mazegen import generator
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
if __name__ == "__main__":
    grid = generator.create_closed_grid(30, 30)
    blocked = generator.get_pattern_cells(30, 30)
    rng = random.Random(1)
    generator.carve_maze(grid, 30, 30, rng, blocked)
    for row in grid:
        print("".join(f"{c:X}" for c in row))