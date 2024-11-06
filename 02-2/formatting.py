# 문자열 포매팅(string formatting)
'''
%s = 문자열(string)
%c = 문자 1개(charactor)
%d = 정수(integer)
%f = 부동소수(floating-point)
%o = 8진수
%x = 16진수
%% = Literal(문자 % 자체)
'''

# 예제1 숫자 바로 대입
print("I eat %d apples." % 3)

# 예제2 문자 바로 대입
print("I eat %s apples." % "five")

# 예제3 숫자 값을 나타내는 변수로 대입 
number = 3
print("I eat %d apples." % number)

# 예제4 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 예제5 %s 포맷코드 - 어떤 형태의 값이든 변환해 넣을 수 있다
print("I have %s apples." % 3)
print("rate is %s" % 3.234)

# 예제6 문자열 포맷코드와 %가 같은 문자열에 있다면 %% 사용
print("Error is %d%%." % 98)

# 예제7 포맷 코드와 숫자 함께 사용하기 - 정렬과 공백(오른쪽 정렬)
print("%10s" % "hi")

# 예제8 포맷 코드와 숫자 함께 사용하기 - 정렬과 공백(왼쪽 정렬)
print("%-10sjane" % "hi")

# 예제9 포맷 코드와 숫자 함께 사용하기 - 소수점 표현하기(소수점 네 번째 자리까지 나타내기)
print("%0.4f" % 3.42134234)

# 예제10 포맷 코드와 숫자 함께 사용하기 - 소수점 표현하기(공백과 소수점 자릿수 지정)
print("%10.4f" % 3.42134234)