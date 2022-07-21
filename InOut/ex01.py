#표준입출력
print("Python", "Java")     #콤마로 구분시, 자동으로 띄어쓰기
print("Python" + "Java")    # 플러스로 연결시, 그냥 붙여서 출력

print("Python", "Java", sep=",")    #내가 원하는 방식으로 구분 가능
print("Python", "Java", "JavaScript", sep=" vs ")

print("Python", "Java", sep=",", end="?")   #end 문장의 끝을 원하는 방식으로 변경가능
print("무엇이 더 재밌을까요?")



# import sys
# print("Python", "Java", file=sys.stdout)    #표준출력
# print("Python", "Java", file=sys.stderr)    #표준에러



# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():   #여기서 subject는 키, score는 value
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #.ljust : (8)칸 자리 확보 후, 왼쪽 정렬
    #.rjust : (4)칸 자리 확보, 오른쪽 정렬



# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    #.zfill : (3)자리 숫자로 만들고 나머지는 0으로 채움



answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")