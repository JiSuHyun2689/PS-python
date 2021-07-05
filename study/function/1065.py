from sys import stdin


def han_number(x):
    count = pow(10, 2) - 1

    if x < 100:
        count = x
    else:
        for i in range(100, x + 1):
            x_list = list(map(int, str(i)))
            if x_list[2] - x_list[1] == x_list[1] - x_list[0]:
                count += 1
    return count


x = int(stdin.readline())
print(han_number(x))
