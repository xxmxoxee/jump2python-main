# 조건부 표현식

'''score가 60 이상일 경우 message에 문자열 "success", 아닐 경우에는 문자열 "failure"를 대입하는 코드'''

score = 50

if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)


# 조건부 표현식을 사용한 코드
message = 'success' if score >= 60 else 'failure'
'''변수 = 조건문이 참인 경우의 값 if 조건문 else 조건문이 거짓인 경우의 값'''
print(message)