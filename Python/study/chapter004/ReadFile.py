
try:
    readFile = open('hello.txt', 'r')
except Exception as err:
    print("exception {0}".format(err) )
else:
    temp = readFile.read()
    print(temp)
    readFile.close()
