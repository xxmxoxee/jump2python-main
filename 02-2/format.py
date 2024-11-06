# format 함수를 사용한 포매팅


# 예제1 숫자 바로 대입 - format 함수 사용 전
print("I eat %d apples." % 3)

# 예제1 숫자 바로 대입 - format 함수 사용 후
print("I eat {0} apples." .format(3))
print("-" * 60)



# 예제2 문자 바로 대입 - format 함수 사용 전
print("I eat %s apples." % "five")

# 예제2 문자 바로 대입 - format 함수 사용 후
print("I eat {0} apples." .format("five"))
print("-" * 60)



# 예제3 숫자 값을 나타내는 변수로 대입 - format 함수 사용 전
number = 3
print("I eat %d apples." % number)

# 예제3 숫자 값을 나타내는 변수로 대입 - format 함수 사용 후
number = 3
print("I eat {0} apples." .format(number))
print("-" * 60)



# 예제4 2개 이상의 값 넣기 - format 함수 사용 전
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 예제4 2개 이상의 값 넣기 - format 함수 사용 후
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))

# 예제4 2개 이상의 값 넣기 - format 함수에 이름으로 넣기
number = 10
day = "three"
print("I ate {number} apples. so I was sick for {day} days." .format(number=10, day="three"))

# 예제4 2개 이상의 값 넣기 - format 함수 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} Days." .format(10, day="three"))
print("-" * 60)



# 예제7 포맷 코드와 숫자 함께 사용하기 - 정렬과 공백(오른쪽 정렬) - format 함수 사용 전
print("%10s" % "hi")

# 예제7 포맷 코드와 숫자 함께 사용하기 - 정렬과 공백(오른쪽 정렬) - format 함수 사용 전
print("{0:>10}" .format("hi"))
print("-" * 60)



# 예제8 포맷 코드와 숫자 함께 사용하기 - 정렬과 공백(왼쪽 정렬) - format 함수 사용 전
print("%-10sjane" % "hi")

# 예제8 포맷 코드와 숫자 함께 사용하기 - 정렬과 공백(왼쪽 정렬) - format 함수 사용 전
print("{0:<10}jane" .format("hi"))
print("-" * 60)



# 예제8-1 format 함수 가운데 정렬
print("{0:^10}" .format("hi"))
print("-" * 60)



# 예제9 포맷 코드와 숫자 함께 사용하기 - 소수점 표현하기(소수점 네 번째 자리까지 나타내기) - format 함수 사용 전
print("%0.4f" % 3.42134234)

# 예제9 포맷 코드와 숫자 함께 사용하기 - 소수점 표현하기(소수점 네 번째 자리까지 나타내기) - format 함수 사용 후
y = 3.42134234
print("{0:0.4f}" .format(y))
print("-" * 60)



# 예제10 포맷 코드와 숫자 함께 사용하기 - 소수점 표현하기(공백과 소수점 자릿수 지정) - format 함수 사용 전
print("%10.4f" % 3.42134234)

# 예제10 포맷 코드와 숫자 함께 사용하기 - 소수점 표현하기(공백과 소수점 자릿수 지정) - format 함수 사용 후
y = 3.42134234
print("{0:10.4f}" .format(y))
print("-" * 60)