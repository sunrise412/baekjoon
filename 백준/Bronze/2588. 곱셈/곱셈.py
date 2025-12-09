a = int(input())
b = int(input())

for i in reversed(str(b)):
    print(a*int(i))
print(a*b)