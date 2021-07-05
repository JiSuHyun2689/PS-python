import sys;
n, x = map(int, sys.stdin.readline().split())
result = [ num for num in sys.stdin.readline().split() if int(num) < x ];
print(" ".join(result))