n = int(input())
parts = set(map(int, input().split()))
m = int(input())
need_parts = list(map(int, input().split()))

for i in need_parts:
    if i in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')