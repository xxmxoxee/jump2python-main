# for 문과 함께 자주 사용하는 range 함수

a = range(10)
print(a)
'''range(시작_숫자, 끝_숫자) 이때 끝 숫자는 포함되지 않는다.'''

# 예시
add = 0
for i in range(1, 11):
    add = add + i

print(add)

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')