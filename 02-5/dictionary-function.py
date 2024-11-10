# 딕셔너리 관련 함수

# keys - key리스트 만들기
a = {'name': 'pey', 'phone': '010-1111-1111', 'birth': '1118'}
print(a.keys())
print(list(a.keys())) # 리스트로 반환하고싶다면

''' 사용 예
for k in a.keys():
  print(k)
'''

# values - value리스트 만들기
print(a.values())

# items - key, value 쌍 얻기
print(a.items())

# clear - key: value 쌍 모두 지우기
print(a.clear())

# get - key로 value 얻기
a = {'name': 'pey', 'phone': '010-1111-1111', 'birth': '1118'}
print(a.get('name'))
print(a.get('nokey')) 
'''
딕셔너리에 값이 없을 경우 
a['nokey'] 방식은 오류를 발생시키고 a.get('nokey')방식은 none을 리턴한다.
'''
print(a.get('nokey', 'foo')) # 값이 없을 경우 디폴트값을 설정할 수 있다

# in - 해당 key가 딕셔너리 안에 있는지 조사하기
a = {'name': 'pey', 'phone': '010-1111-1111', 'birth': '1118'}
print('name' in a)
print('email' in a)
