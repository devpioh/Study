def getPrime(x):
    for i in range(2, x-1 ):
        if x % i == 0:
            break
        else:
            return x

def InputData():
    numberList = list()

    while(True):
        data = input('input number (stop input -> q): ') 
        if 'q' == data:
            break
        elif 0 != int(data) and 0 < int(data):
            numberList.append(int(data))
        else:
            print('please input integer!\n')

    return numberList


numbers = InputData()
ret = filter(getPrime, numbers)

print('<numberList>')
print(numbers)
print('<primeList>')
print(list(ret))


