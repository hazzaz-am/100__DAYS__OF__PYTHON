# Explicit type casting
a = "12"
b = "45"
print(int(a) + int(b))

a = 23.32
b = "23.32"
print(int(a) + int(float(b)))

a = 5 # True
a = -5 # True
a = -0 # False
a = 0 # False
print(bool(a))
print(type(a))

s = 45
s = 4.5
s = True
print(str(s))
print(type(s))


# Implecit type casting

a = 34.43
b = 50
print(a + b)
print(type(a + b))
 