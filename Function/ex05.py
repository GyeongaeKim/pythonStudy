#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     #end=" "  줄바꿈 없이, 따옴표 안의 내용으로 연결
#     print(lang1, lang2, lang3, lang4, lang5)

#다른 갯수의 값을 넣을때는 *(가변인자)를 사용!!
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "kotlin", "Swift")