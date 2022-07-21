# pickle
# 프로그램 상에서 우리가 사용하고 있는 데이터를 file형태로 저장해주는 것.

import pickle
profile_file = open("profile.pickle", "wb")
#wb = 바이너리 타입, 피클쓸때 꼭!!

profile = {}