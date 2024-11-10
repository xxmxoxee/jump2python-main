# 튜플 - 요솟값을 변경X

'''
튜플 요솟값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
del t1[0]
TypeError: 'tuple' object doesn't support item deletion
'''

'''
튜플 요솟값을 변경하려 할 때
t1 = (1, 2, 'a', 'b')
t1[0] = 'c'
TypeError: 'tuple' object does not support item assignment
'''

# 튜플 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 튜플 슬라이싱
t1 = (1, 2, 3, 4, 5)
print(t1[1:])

# 튜플 더하기
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)

# 튜플 곱하기
t1 = (1, 2)
t2 = t1 * 3
print(t2)

# 튜플 길이 구하기
t1 = (1, 2, 3, 4, 5, 6)
print(len(t1))

# 문제. (1, 2, 3)이라는 튜플 값에 4를 추가하여 (1, 2, 3, 4)라는 새로운 튜플을 출력해보자
t1 = (1, 2, 3)
t2 = (4,)
t3 = t1 + t2
print(t3)