#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())   #소문자로
print(python.upper())   #대문자로
print(python[0].isupper())  # ...는 대문자인가?
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) #찾은 인덱스 다음 인덱스 찾기(두번째n 찾기)
print(index)

print(python.find("n"))
print(python.find("Java"))  #포함되지 않은 값이면, -1
# print(python.index("Java"))     #없는 값일 경우, 오류가 난다

print(python.count("n"))