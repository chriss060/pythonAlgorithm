input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

move= [(1,2), (1, -2), (-1,2), (-1,-2), (2, 1), (-2, 1), (-2, -1), (2, -1),(-1, 2)]


count = 0

for m in move:
    nrow = row + m[0]
    ncol = column + m[1]

    if nrow >= 1 and nrow <= 8 and ncol >= 1 and nrow <= 8:
        count += 1

print(count)