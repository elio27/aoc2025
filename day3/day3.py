def total_joltage(lines, n):

    total_output_joltage = 0

    for line in lines:
        int_line = list(map(int, list(line)))
        curr_str = ""
        curr_index = 0

        for i in range(n):
            d = max(int_line[curr_index : len(line)-(n-i-1)])
            curr_index = int_line.index(d, curr_index) + 1
            curr_str += str(d)

        total_output_joltage += int(curr_str)
    return total_output_joltage

with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

total_2_digits = total_joltage(lines, 2)
total_12_digits = total_joltage(lines, 12)

print(f"Total Output Joltage for 2 digits: {total_2_digits}")
print(f"Total Output Joltage for 12 digits: {total_12_digits}")
