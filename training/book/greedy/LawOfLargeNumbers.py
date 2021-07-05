# N, M, K 공백으로 구분하여 입력 받기
# N개의 수를 공백으로 구분하여 입력 받기
# 5 8 3
# 2 4 5 4 6

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
a = int(m / (k+1)) * k
b = m % k

print(a * data[n-1] + b * data[n-2])