# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# print(cabinet[5])   #대괄호 사용시, 오류 -> 종료
# print("hi")

print(cabinet.get(5))   #.get() 사용시, 오류 -> None 출력
print(cabinet.get(5, "사용 가능"))  #None 대신 다른 내용 출력
print("hi")


print(3 in cabinet)   # True
print(5 in cabinet)   # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"      #이미 값이 있었다면, 값 없데이트됨
cabinet["C-20"] = "조세호"
print(cabinet)


# 간 손님
del cabinet["A-3"]
print(cabinet)


# key 들만 출력하기
print(cabinet.keys())
# value 들만 출력하기
print(cabinet.values())
# key, value 쌍으로 출력하기
print(cabinet.items())


# 목욕탕 폐점
cabinet.clear()
print(cabinet)