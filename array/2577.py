import sys;

num = 1;

for i in range(3):
    num *= int(sys.stdin.readline())

nums = [int(x) for x in str(num)]

for i in range(0, 10):
    print(nums.count(i))
