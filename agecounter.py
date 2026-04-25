ages = [18, 18, 15, 15, 14, 10, 9, 20, 23, 8]

between = 0
above = 0
below = 0

for i in ages:
    if i >= 18 and i <= 20:
        between += 1
    elif i > 21:
        above += 1
    else:
        below += 1


print("Ages between 18 - 20 = ", between)
print("Ages above 20 = ", above)
print("Ages below 18 = ", below)
