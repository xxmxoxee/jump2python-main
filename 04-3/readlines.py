# readlines.py
f = open("/Users/doheekim/Desktop/dev/jump2python-main/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
