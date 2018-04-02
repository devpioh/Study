file = open("hello.txt", 'w')
file.write('hello')
file.close

try:
    readFile = open('hello.txt', 'r')
except Exception as err:
    print("exception {0}".format(err) )
else:
    temp = readFile.read()
    print(temp)
    readFile.close()


