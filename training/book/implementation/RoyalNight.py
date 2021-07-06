data = input()
x = int(ord(data[0])) - int(ord('a')) + 1
y = int(data[1])
rules = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)];
count = 0

for i in rules:
    nx = x + i[0]
    ny = y + i[1]
    if(nx < 1 or nx > 8 or ny < 1 or ny > 8):
        continue
    count += 1

print(count)