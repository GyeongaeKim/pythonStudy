#집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)   #중복은 허용하지 않는다


# 교집합 (java와 python을 모두 할 수 있는 사람)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))


# 합집합 (java 할 수 있거나, python 할 수 있는 사람)
print(java | python)
print(java.union(python))


#차집합 (java는 할 수 있지만, python은 할 수 없는 사람)
print(java - python)
print(java.difference(python))


# python 할 줄 아는 사람이 늘어났다!
python.add("김태호")       #set에 값 추가 가능
print(python)


# java 를 까먹었어요!
java.remove("김태호")
print(java)