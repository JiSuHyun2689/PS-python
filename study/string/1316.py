from sys import stdin

check = 0

for case in range(int(stdin.readline())):
    word = stdin.readline().strip()
    word_len = len(word)

    for idx in range(word_len):
        if idx != word_len-1 and word[idx] == word[idx + 1]:
            # 단어의 맨 마지막이 아니고, 연속된 문자이면 continue
            continue
        elif word[idx+1:].count(word[idx]) != 0:
            # 현재 판별 중인 알파벳이 단어에 포함되어 있으면 그룹 단어가 아니므로 for 문 벗어남
            break
        elif idx == word_len-1:
            # 단어의 맨 마지막까지 왔다면 그룹 단어이므로 갯수 count
            check += 1

print(check)
