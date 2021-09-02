# 한 번 계산된 결과를 메모제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(Top Down Dynamic Programming)
def fibo(x):
    print('f(' + str(x) +')', end=' ')
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있다면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산한 적 없다면 점화식에 따라 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# 5000번째 이상의 큰 피보나치 수를 구할 경우 '재귀 함수 깊이 (recursion depth)'와 관련된 오류 발생
# 이 경우 sys 라이브러리에 포함된 setrecursionlimit() 함수를 호출하여 재귀 제한 완화 가 능