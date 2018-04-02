
#integer number
print("integer number")
int_data = 10
bin_data = 0b10
oct_data = 0o10
hex_data = 0x10
long_data = 1234567890123456789

print(int_data)
print(bin_data)
print(oct_data)
print(hex_data)
print(long_data)
print("")

#real number
print("real number")
f1 = 1.0
f2 = 3.14
f3 = 1.56e3
f4 = -0.7e-4

print(f1)
print(f2)
print(f3)
print(f4)
print("")

#imaginary number
print("imaginary number")
c1 = 1+7j
c2 = complex(2, -3)

print("1+7j => real : %d,  imag : %d", c1.real, c1.imag )
print( c2 )