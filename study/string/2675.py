from sys import stdin

for i in range(int(stdin.readline())):
    print_str = ""
    num, string = list(stdin.readline().strip("\n").split())
    for temp in string:
        print_str += temp * int(num)
    print(print_str)