from sys import stdin;

for _ in range(int(stdin.readline())):
    input_list = list(map(int, stdin.readline().split()))
    avg = sum(input_list[1:len(input_list)]) / input_list[0]
    print("%.3f%%" % round(sum(map(lambda score: score > avg, input_list[1:len(input_list)])) / input_list[0] * 100, 3))

    # num = input_list[0]
    # del input_list[0]
    # avg = sum(input_list) / num
    # count = 0
    #
    # for score in input_list:
    #     if score > avg:
    #         count = count + study
    #
    # print("%.3f%%" % round(count/num * 100, 3))


