list = [2, 3, 3, 6, 7, 8, 9, 9, 11, 12, 13, 17, 22, 2, 22]
x = []
for num in list:
    if num not in x:
        x.append(num)
print(x)