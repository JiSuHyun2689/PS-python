def CountSort(array):
    for i in range(len(array)):
        temp[array[i]] = 1

n = int(input())
parts = list(map(int, input().split()))
m = int(input())
need_parts = list(map(int, input().split()))
temp = [0] * (max(parts) + 1)

CountSort(parts)

for i in range(len(need_parts)):
    if temp[i+1] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')


