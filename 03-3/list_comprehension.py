# 리스트 컴프리헨션

''' 문법
[표현식 for 항목 in 반복_가능_객체 if 조건문]
[표현식 for 항목1 in 반복_가능_객체 if 조건문1
      for 항목2 in 반복_가능_객체 if 조건문2
      ...
      for 항목n in 반복_가능_객체 if 조건문n
      ]
'''

# 사용 전
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)

# 사용 후
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)

# 짝수에만 3을 곱하고 싶다면
a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2 == 0]
print(result)