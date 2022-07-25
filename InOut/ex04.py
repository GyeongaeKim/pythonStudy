# pickle
# 프로그램 상에서 우리가 사용하고 있는 데이터를 file형태로 저장해주는 것.


import pickle

#1. pickle파일 만들기

profile_file = open("profile.pickle", "wb")
#wb = 바이너리 타입, 피클쓸때 꼭!!

profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)      # profile에 있는 정보를 file에 저장
profile_file.close()        # profile.pickle 파일생성됨ㅋㅋ



#2. pickle파일 가져오기

profile_file = open("profile.pickle", "rb")     # rb 읽기, 바이너리 타입
profile = pickle.load(profile_file)     # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
