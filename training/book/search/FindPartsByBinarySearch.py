def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
parts = list(map(int, input().split()))
parts.sort()
m = int(input())
need_parts = list(map(int, input().split()))
temp = [0] * (max(parts) + 1)

for i in need_parts:
    result = binary_search(parts, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')