import sys
import os

option = sys.argv[1]
memo = sys.argv[2]

print(option)

memoDir = '/CTMemo/Memos/'

if option =='-w':
    if False == os.path.exists(memoDir + 'memo.txt'):
        os.makedirs(memoDir)
    f = open(memoDir+'memo.txt', 'a')
    f.write(memo + '\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

