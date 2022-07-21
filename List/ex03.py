#튜플 - 변경 불가/ 값 추가 불가(add)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")   추가 불가

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)


#한번에 담아주기
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)