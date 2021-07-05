# import sys;
# for i in range(int(sys.stdin.readline()) , 0, -study):
#     print(i);

n = int(input())
print("\n".join(map(str, range(n, 0, -1))))