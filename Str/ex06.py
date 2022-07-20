#Quiz/ 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# ex - http://naver.com
# 규칙1 : http:// 부분은 제외  ->  naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외  ->  naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# ex - 생성된 비밀번호 : nav51!

# 내가 푼것.
site = "http://naver.com"
print(site[7:])
print(site[7:-4])

left = site[7:-4]
print(left[:3])
print(left.count("e"))

result = print(left[:3],left.count("e"),"!")




# 문제 풀이
url = "http://naver.com"
url = "http://google.com"
url = "http://youtube.com"
my_str = url.replace("http://", "")     #규칙1
print(my_str)

my_str = my_str[:my_str.index(".")]     #처음부터 점이 있는 곳까지 자른다.
print(my_str)   #규칙2

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

