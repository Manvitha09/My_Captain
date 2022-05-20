n = int(input("Number of elements in fibonacci series"))
a =0
b =1
s = 0
print(a)
print(b)
for i in range (2,n):
    s = a+b
    a = b
    b = s
    print(s)
