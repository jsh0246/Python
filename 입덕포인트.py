a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

l = a if a > b else b

print(l)