def d(n):
    return n + sum(int(i) for i in str(n))


self_number_list = set(range(1, 10001))
make_number_list = set()

for i in range(1, 10001):
    make_number_list.add(d(i))

self_number_list = self_number_list - make_number_list

for i in sorted(self_number_list):
    print(i)
