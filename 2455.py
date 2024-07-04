a, b= map(int, input().split())
c, d= map(int, input().split())
e, f= map(int, input().split())
g, h= map(int, input().split())
li = [b, b+d-c, b+d-c+f-e]

print(max(li))
