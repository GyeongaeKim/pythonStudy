#Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓을은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

"""
(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --
"""

""" (활용 예제)
from random import * 
lst = [1, 2, 3, 4, 5]
print(lst)

shuffle(lst)    #lst의 값 순서를 무작위로 변경
print(lst)

print(sample(lst, 1))   #lst 중에서 1개를 무작위로 뽑기
"""




from random import *
users = range(1, 21)    #1부터 21직전까지(1~20)
print(type(users))      #type은 range
users = list(users)     #리스트 타입으로 변경
print(type(users))


print(users)
shuffle(users)  #셔플로 순서 바꿔주기
print(users)


winners = sample(users, 4)      # 4 명 중에서 1명은 치킨, 3명은 커피


print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))    #당첨자 4명 중 첫번째
print("커피 당첨자 : {0}".format(winners[1:]))      #치킨 당첨자 제외 나머지 당첨자
print("-- 축하합니다 --")


