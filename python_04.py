def add(num1, num2):
    return num1 + num2

result1 = (add(10, 20))

def add(num1, num2, num3, num4):
    return num1 + num2, num3 + num4

result2 = add(10, 20, 30, 40)
print(result2) #튜플(리턴 => 하나의 값을 리턴)

r1, r2 = (1, 2)
print (r1, r2)

nums = [5, 2, 4, 6, 9]
nums.sort()
nums.reverse()
print(nums)

# print(nums.index(10))
# name = "홍길일"
# print(name.find("이"))
# print(name.index("이"))

user = {
    "username" : "testuser",
    "password" : "1234",
    "name" : "짱구",
    "email" : "Wkdrn@naver.com"
}

print(user)
user.update({
    "phone": "010-1234-5678",
    "name" : "훈발롬"
})
user["age"] = 31
print(user)

