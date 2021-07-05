from sys import stdin
import string

word_list = list(stdin.readline().strip("\n"))

for alphabet in string.ascii_lowercase:
    if alphabet not in word_list:
        print(-1)
    else:
        print(word_list.index(alphabet))

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(str(word_list).find(i), end=' ')