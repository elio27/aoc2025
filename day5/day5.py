fresh_ranges = []

with open('input.txt', 'r') as f:
    p1, p2 = f.read().split('\n\n')

    ranges = p1.split('\n')
    ids = list(map(int, p2.split('\n')))

    for r in ranges:
        a, b = r.split('-')
        fresh_ranges.append([int(a), int(b)])

# Part 1
fresh_count_1 = 0

for id in ids:
    for a, b in fresh_ranges:
        if a <= id <= b:
            fresh_count_1 += 1
            break

# Part 2
fresh_ranges.sort(key=lambda x: x[0])

merged = [fresh_ranges[0]]

for a, b in fresh_ranges:
    last = merged[-1]
    if a <= last[1] + 1:
        last[1] = max(last[1], b)
    else:
        merged.append([a, b])

fresh_count_2 = sum([b - a + 1 for a,b in merged])


print(fresh_count_1)
print(fresh_count_2)
