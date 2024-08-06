a1, a2 =map(int, input().split())
b1, b2 =map(int, input().split())
c1, c2 =map(int, input().split())
p=int(input())
k=0
while p<=0:
    if k%a1==0:
        p-=a2
    if k%b1==0:
        p-=b2
    if k%c1==0:
        p-=c2
print(k)