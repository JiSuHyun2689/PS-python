import sys;

num = int(sys.stdin.readline());

for i in range(num):
    quiz = list(sys.stdin.readline().strip('\n'))
    count, sum = 0, 0

    for idx, word in enumerate(quiz):
        if word == 'O':
            count += 1
            sum += count
        else :
            count = 0
    print(sum)
