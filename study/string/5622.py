from sys import stdin

input_string = stdin.readline().strip()
dial_set = [[],["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M","N","O"],["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"], ["OPERATOR"]]
num = 0

for string in input_string:
    for idx, dial in enumerate(dial_set):
        if string in dial:
            num += idx + 2
print(num)