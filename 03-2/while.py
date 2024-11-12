# while 반복문

''' "열 번 찍어 안 넘어가는 나무 없다" 라는 속담을 파이썬 프로그램으로 만들면
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')
'''


''' 여러가지 선택지 중 하나를 선택해 입력받는 예제
prompt = """
1. Add
2. Del
3. List
4. Quit
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())
'''


''' while 문 강제로 빠져나가기
coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee - 1
    print('남은 커피의 양은 %d개 입니다.' % coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break
'''


''' while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
'''


''' 1부터 10까지의 숫자 중에서 3의 배수를 뺸 나머지 값을 출력해 보자.
a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)
'''