a = b'r\xc3\xa9sum\xc3\xa9'

print(a.decode("utf-8"))
a = a.decode("utf-8")

print(a.encode("Latin1"))
a = a.encode("Latin1")

print(a.decode("Latin1"))
