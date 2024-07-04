a = int(input())
b = int(input())
c = int(input())
d=a+b+c
if d ==180:
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")