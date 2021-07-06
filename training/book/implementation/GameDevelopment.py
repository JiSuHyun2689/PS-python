n, m = 4, 4
d = [[0] * m for _ in range(n)]
x, y, direction = 1, 1, 0
d[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
array = [(1,1,1,1), (1,0,0,1), (1,1,0,1), (1,1,1,1)]

def turn_left():
    global direction
    direction -= 1      # 왼쪽으로 방향 전환
    if direction == -1:
        direction = 3   # -1은 서쪽 = 3

count = 1
turn_time = 0
while True:
    turn_left()             # 방향 전환
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0 : ## 전환 방향에 가보지 않은 칸이 있다면 이동
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 회전 후 앞에 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
