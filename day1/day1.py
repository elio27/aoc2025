with open("./input.txt") as f: inp = f.read()

dial = 50
zeros = 0
clicks = 0
for instr in inp.splitlines():
    turn = instr[0]
    dist = int(instr[1:])
    if dist >= 100:
        clicks += dist//100
        dist %= 100

    if turn == "L":
        if dist >= dial != 0:
            clicks += 1
        dial -= dist
    else:
        if dist >= 100-dial and dial!=0:
            clicks += 1
        dial += dist

    dial %= 100
    if dial == 0: zeros += 1

print("Zeros:",zeros)
print("Clicks:", clicks)