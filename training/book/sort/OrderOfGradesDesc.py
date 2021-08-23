n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

def printArray(array):
    for student in array:
        print(student[0], end=' ')


array = sorted(array, key=lambda student : student[1])
print("오름차순")
printArray(array)

array = sorted(array, key=lambda student: student[1], reverse=True)
print("\n내림차순")
printArray(array)
