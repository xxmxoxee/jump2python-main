# 리스트 관련 함수

# append 추가
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

# sort 정렬
a = [1, 4, 5, 3]
a.sort()
print(a)

a = ['a', 'c', 'e', 'b']
a.sort()
print(a)

# reverse 리스트 뒤집기
a = ['a', 'e', 'z']
a.reverse()
print(a)

# index 인덱스 반환
a = [1, 2, 3]
print(a.index(3))
''' print(a.index(0)) 리스트에 없는 값이기 때문에 ValueError: 0 is not in list 오류 발생 함 '''

# insert 리스트에 요소 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

# remove 리스트 요소 제거 - 리스트에서 첫 번째로 나오는 x 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)

# pop 리스트 요소 끄집어 내기 - 마지막 요소를 리턴하고 그 요소는 삭제
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

# count 리스트에 포함된 요소의 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

# extend 리스트의 확장
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)