#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

#키워드도 함께 입력하면, 순서가 뒤바뀌어도 출력에 문제가 없다
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")