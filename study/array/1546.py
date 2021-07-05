import sys;

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max_score = max(scores)

for idx, score in enumerate(scores):
    scores[idx] = score/max_score*100

print(sum(scores)/n)

# n = int(sys.stdin.readline())
# *scores, = map(int, sys.stdin.readline().split())
# print(sum(scores)*100 / max(scores) / n)