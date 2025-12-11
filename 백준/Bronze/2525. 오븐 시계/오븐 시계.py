a, b = map(int, input().split())
c = int(input())

if c >=60:
    h = c//60
    m = c%60
else:
    h = 0
    m = c

a += h
b += m

if b >= 60:
    a += 1
    b -= 60

if a >= 24:
    a -= 24
    
print(a, b)