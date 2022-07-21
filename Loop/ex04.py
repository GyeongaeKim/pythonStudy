# continue, break
absent = [2, 5]     #결석
no_book = [7]   #책을 깜빡한 학생
for student in range(1, 11):        #1~10번까지의 학생들이 있다.
    if student in absent:       #만일 학생이 결석을 했다면,
        continue            #결석한 학생 제외하고 반복 - 다음 반복문 진행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break       #break - 뒤에 반복문이 있든없든, 바로 종료
    print("{0}, 책을 읽어봐".format(student))

