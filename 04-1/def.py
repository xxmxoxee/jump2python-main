# 함수

'''
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2

    return 리턴값
'''

# 기본
def add(a, b):
    return a + b

print(add(3, 5))

# 입력값이 없는 경우
def say():
    return 'HI'

print(say())

# 리턴값이 없는 경우
def add(a, b):
    print('%d, %d의 합은 %d입니다.' % (a, b, a + b))

print(add(3, 7)) # 리턴값이 없어서 None도 함께 출력 됨

# 입력값도 리턴값도 없는 함수
def say():
    print('HI')

print(say())

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)

print(result)

# 여러개의 입력값을 받는 함수 만들기
''' 매개변수 앞에 *을 붙이면 입력 받은 모든 매개변수를 튜플로 만들어준다 '''
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3, 4, 5)
print(result)

# 키워드 매개변수
def print_kwargs(**kwargs):
    print(kwargs)

print(print_kwargs(a=1))