#ex_1
a = 3
b = a
c = a
print(id(a), id(b), id(c))
#ex_2
a = 5
b = [a]
print(id(a), id(b))
#ex_3
a = 3
b = str(a)
c = [a]
print(id(a), id(b), id(c))

a = 5
b = a
print(id(a), id(b))