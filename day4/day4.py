with open("input.txt", 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]

r, c = len(grid), len(grid[0])

removed = 0
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]

while True:
    to_remove = []

    for x in range(r):
        for y in range(c):
            if grid[x][y] == '@':
                n = 0
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < r:
                        if grid[nx][ny] == '@':
                            n += 1
                if n < 4:
                    to_remove.append((x, y))

    if removed == 0: print("Initial accessible rolls:", len(to_remove))
    if not to_remove: break

    removed += len(to_remove)
    for x, y in to_remove:
        grid[x][y] = '.'

print(f"Total rolls removed: {removed}")
