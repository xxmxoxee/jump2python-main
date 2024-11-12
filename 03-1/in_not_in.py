# in, not in 연산자

'''
x in 리스트
x in 튜플
x in 문자열
x not in 리스트
x not in 튜플
x not in 문자열
'''

print(1 in [1, 2, 3]) # 1이 [1, 2, 3] 안에 있는가? True
print(1 not in [1, 2, 3]) # 1이 [1, 2, 3] 안에 없는가? False

'''만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라'''
poket = ['paper', 'cellphone', 'money']
if 'money' in poket:
    print('택시를 타고 가라')
else:
    print('걸어가라')

'''만약 주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라'''
poket = ['card', 'cellphone', 'money']
if 'card' not in poket:
    print('걸어가라')
else:
    print('버스를 타고 가라')