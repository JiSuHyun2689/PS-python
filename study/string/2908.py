from sys import stdin

a, b = stdin.readline().split()

print(max(a[::-1], b[::-1]))

# a = list(str(a))
# b = list(str(b))
#
# a.reverse()
# b.reverse()
#
# a = ''.join(a)
# b = ''.join(b)
#
# print(a if a>b else b)


