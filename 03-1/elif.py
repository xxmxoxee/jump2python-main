# elif

'''주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.'''
poket = ['paper', 'cellphone']
card = True
if 'money' in poket:
    print('택시를 타고 가라.')
else:
    if card:
        print('택시를 타고 가라.')
    else:
        print('걸어가라')


# elif로 바꾸기
poket = ['paper', 'cellphone']
card = True
if 'money' in poket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# 한 줄로 쓰기
poket = ['paper', 'money', 'cellphone']
if 'money' in poket: pass
else: print('카드를 꺼내라')