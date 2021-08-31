def binary_search(array, target, start, end):
    # 종료 조건
    if start > end:
        return None
    mid = (start + end) // 2

    # target 찾은 경우 중간 지점 반환
    if array[mid] == target:
        return mid
    # 중간 지점이 target 보다 큰 경우 왼쪽 범위 탐색
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간 지점이 target 보다 작은 경우 오른쪽 범위 탐색
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)

# 원소의 개수 n, target 문자열 입력 받기
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("target이 리스트에 존재하지 않습니다.")
else:
    print(result+1)
