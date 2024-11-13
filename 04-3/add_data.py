# add_data.py
f = open("/Users/doheekim/Desktop/dev/jump2python-main/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
