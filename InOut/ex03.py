# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8")
#open을 통해서 파일을 열 수 있다
#("파일이름", "w = write", encoding="")

print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()  #파일을 열었으면 닫아주기까지 해야됨


score_file = open("score.txt", "a", encoding="utf8")
# ("파일이름", "a = append 기존 내용에 추가해서 쓰기", encoding="")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")  #.write는 줄바꿈이 알아서되지는 않음
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
# ("파일이름", "r = read", encoding="")
print(score_file.read())    #한 번에 다 읽기
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())    #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
#print에서는 줄바꿈이 자동으로 되기때문에, 싫으면 end=" "추가
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
#파일이 총 몇줄인지 모를때에는 while문으로 출력하면 된다.
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()



score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()      #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()