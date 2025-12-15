from collections import defaultdict

with open("input.txt", 'r') as f:
    grid = [line.strip() for line in f.readlines()]

start_col = grid[0].index('S')

current_beams = [start_col]
total_splits = 0
h = len(grid)
w = len(grid[0])

for r in range(1, h):
    next_beams = []

    for col in current_beams:
        if col < 0 or col >= w: continue

        char = grid[r][col]

        if char == '^':
            total_splits += 1
            if col - 1 not in next_beams:
                next_beams.append(col - 1)
            if col + 1 not in next_beams:
                next_beams.append(col + 1)
        else:
            if col not in next_beams:
                next_beams.append(col)

    current_beams = next_beams

    if not current_beams: break

current_timelines = defaultdict(int)
current_timelines[start_col] = 1
for r in range(1, h):
    next_timelines = defaultdict(int)

    for col, count in current_timelines.items():

        char = grid[r][col]
        targets = []

        if char == '^':
            targets.append(col - 1)
            targets.append(col + 1)
        else:
            targets.append(col)

        for t_col in targets:
            next_timelines[t_col] += count

    current_timelines = next_timelines


total_finished_timelines = sum(current_timelines.values())

print(total_splits)
print(total_finished_timelines)
