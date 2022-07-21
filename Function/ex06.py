# #지역변수와 전역변수
gun = 10    #전역변수

#global - 밖의 전역변수를 안의 지역변수로 가져오기
def checkpoint(soldiers):   #경계근무
    global gun  #전역 공안게 있는 gun 사용 - 밖에 있는 변수(전역변수)를 안에서도 사용하게(지역변수)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)   #2명이 경계근무 나감
print("남은 총 : {0}".format(gun))



# 파라미터로 변수 받는 방식을 쓰자
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)   #2명이 경계근무 나감
print("남은 총 : {0}".format(gun))


