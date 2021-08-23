array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
temp = [0] * (max(array) + 1)

for i in range(len(array)):
    temp[array[i]] += 1

for i in range(len(temp)):
    for j in range(temp[i]):
        print(i, end=' ')


