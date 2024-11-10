# 집합 자료형

# 기본형태
s1 = set([1, 2, 3])
print(s1)

s2 = set('hello')
print(s2)

# 인덱싱으로 접근하는 방법
s1 = set([1, 2, 3])
li = list(s1)
print(li)
print(li[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# 교집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))

# 합집합 구하기
print(s1 | s2)
print(s1.union(s2))

# 차집합 구하기
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))
