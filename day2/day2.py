with open("./input.txt") as f: inp = f.read()

s_half = 0
s = 0

for _range in inp.split(','):
    a,b = map(int,_range.split('-'))
    for _id in range(a,b+1):
        s_id = str(_id)
        l = len(s_id)
        if s_id == 2 * s_id[:l//2]:
            s += _id
            s_half += _id
        else:
            for k in range(1, l//2 + 1):
                if l%k == 0 and s_id == s_id[:k] * (l // k):
                    s += _id
                    break

print("Sum of invalid IDs according to the 'repeating twice' rule:", s_half)
print("Sum of invalid IDs according to the 'any repeating sequence' rule:", s)
