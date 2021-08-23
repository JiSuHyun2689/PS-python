array = [('바나나', 2), ('딸기', 6), ('복숭아', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)