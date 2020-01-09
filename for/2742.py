# import sys;
# for i in range(int(sys.stdin.readline()) , 0, -1):
#     print(i);

n = int(input())
print("\n".join(map(str, range(n, 0, -1))))