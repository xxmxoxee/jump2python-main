# sys1.py
# 실행 시 전달받은 인수를 for문을 사용해 차례대로 하나씩 출력하는 예
import sys

args = sys.argv[1:]
for i in args:
    print(i)
