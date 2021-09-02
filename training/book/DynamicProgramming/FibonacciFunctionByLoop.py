# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 첫번째, 두번째 피보나치 수는 1
d[1], d[2] = 1, 1
n = 99

# 피보나치 함수 반복문으로 구현 (Bottom Up Dynamic Programming)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])