with open("input.txt", 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]
    h = len(lines)
    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width) for line in lines]

problems = []
buffer = []

for x in range(max_width):
        col_chars = [grid[y][x] for y in range(h)]
        is_empty_col = all(char == ' ' for char in col_chars)

        if not is_empty_col:
            buffer.append(col_chars)
        elif is_empty_col and buffer:
            problems.append(buffer)
            buffer = []

if buffer: problems.append(buffer)


total_p1 = 0
for i, p_data in enumerate(problems):
    full_text = ""
    p_width = len(p_data)

    for y in range(h):
        row_str = ""
        for x in range(p_width):
            row_str += p_data[x][y]
        full_text += row_str + " "

    tokens = full_text.split()

    numbers = []
    operator = '+' if '+' in tokens else '*'
    numbers = [int(token) for token in tokens if token.isdigit()]

    result = 0
    if operator == '+': result = sum(numbers)
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num

    total_p1 += result

total_p2 = 0
for i, cols in enumerate(problems):
    numbers = []
    operator = '+' if '+' in cols[0] else '*'
    numbers = [int("".join([char for char in col if char.isdigit()])) for col in cols]

    res = 0
    if operator == '+': res = sum(numbers)
    elif operator == '*':
        res = 1
        for n in numbers:
            res *= n
    total_p2 += res

print(total_p1)
print(total_p2)
