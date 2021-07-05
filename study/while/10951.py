import sys;
# while True:
#     line = sys.stdin.readline()
#     if not line: break
#     print(sum(map(int, line.split())))

for line in sys.stdin:
    print(sum(map(int, line.split())))
