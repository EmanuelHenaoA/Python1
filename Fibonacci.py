# serie de fibonacci secuencial

# a = 0
# b = 1
# c = 0

# while a <= 10:
#     c = a + b
#     b = c
#     a = b
#     print(a)

# serie de fibonacci con tuplas o listas

a = 0
b = 1
while a <= 50:
    print(a)
    (a, b) = (b, a + b)
