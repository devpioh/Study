from time import sleep

#progress bar
# for i in range(100):
#     msg = '\r progress %d%%'%(i+1)
#     print( ''*len(msg), end='' )
#     print(msg, end='')
#     sleep(0.1)

#tuple
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c'])
#tuple1[0] = 6

def func():
    print('say hello')

tuple4 = (1, 2, func)
tuple4[2]()