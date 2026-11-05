from mazegen import generator
import random

if __name__ == "__main__":
    grid1 = generator.create_closed_grid(8, 6)
    rng1 = random.Random(1)
    generator.carve_maze(grid1, 8, 6, rng1)
    for row in grid1:
        print("".join(f"{c:x}" for c in row))
    grid2 = generator.create_closed_grid(8, 6)
    rng2 = random.Random(1)
    generator.carve_maze(grid2, 8, 6, rng2)
    print("")
    for row in grid2:
        print("".join(f"{c:x}" for c in row))
    print("")
    if grid1 == grid2:
        print(True)
    else:
        print(False)
