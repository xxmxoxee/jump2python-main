# 딕셔너리 자료형(연관배열, 해시)

# 기본형태
dic = {'name': 'pey', 'phone': '010-1111-1111'}
print(dic)
print(dic['name'])

a = {1: 'hi'}
b = {'a': [1, 2, 3]}
print(b['a'])

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제
del a[1]
print(a)

# Key를 사용해 Value얻기
grade = {'pey': 10, 'julliey': 99}
print(grade['pey'])
print(grade['julliey'])

# 딕셔너리 사용 주의점 - 중복
a = {1: 'a', 1: 'b'}
print(a[1])

# 딕셔너리 사용 주의점 - Key값에 리스트 사용 불가 (단, 값이 변하지 않는 튜플은 사용 가능)
'''
a = {[1, 2]: 'hi'}
print(a)
TypeError: unhashable type: 'list'
'''