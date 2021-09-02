def my_solution(x):
    count = 0
    while x != 1:
        count += 1
        x -= 1
        if x % 5 == 0:
            x //= 5
        if x % 3 == 0:
            x //= 3
        if x % 2 == 0:
            x //= 2
    return count

def solution(x):
    # DP 테이블
    d = [0] * 30001
    # Bottom Up
    for i in range(2, x+1):
        # 현재의 수에서 1 빼는 경우
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    print(d[x])

x = int(input())
print(my_solution(x))
solution(x)