number = 10
print(type(number))

print(id(10)) # id() 주소값 - 리터럴 상수
print(id(number))
number += 1
print(id(number))


print(type("test"))
print(type([]))
print(type(()))
print(type({}))

print([1, 2, 3, 4])
print((1, 2, 3, 4))
print({"id": 1, "name": "홍길동"})

list1 = [1, 2, 3, 4]
tp = (5, 6, 7, 8)
dict1 = {"id": 1, "name": "홍길동"}

print(list1[0])
print(tp[0])
print(dict1["id"])

list1.append(5)
print(list1)

list2 = list(tp) # 형변환
print(list2)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(list(dict1.items())[0])

print(True)
print(False)