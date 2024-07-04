a=0
b=1
tmp =0
c =int(input())
if c== 0:
    print(0)
    exit()
elif c==1:
    print(1)
    exit()

for i in range(c-1):
    tmp = b
    b+=a
    a=tmp

print(b)