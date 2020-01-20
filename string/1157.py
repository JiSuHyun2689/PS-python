from sys import stdin

word = stdin.readline().strip("\n").upper()
word_list = {}
cnt_list = []

for alphabet in set(word):
    word_list[word.count(alphabet)] = alphabet
    cnt_list.append(word.count(alphabet))

print("?" if cnt_list.count(max(cnt_list)) >= 2 else word_list.get(max(cnt_list)))