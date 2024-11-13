# readline_all.py
f = open("/Users/doheekim/Desktop/dev/jump2python-main/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
