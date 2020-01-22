from sys import stdin

input_string = stdin.readline().strip()
croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in croatia_alphabet:
    input_string = input_string.replace(alphabet, "!")
print(len(input_string))

