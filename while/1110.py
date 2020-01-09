import sys;

final_num = int(sys.stdin.readline())
new_num = final_num
count = 0

while True:
    if new_num < 10:
        new_num = int(str(new_num).zfill(2))

    temp = (new_num//10) + (new_num%10)
    new_num = (new_num%10) * 10 + (temp%10)
    count += 1;

    if new_num == final_num:
        print(count)
        break;