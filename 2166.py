import sys
input = sys.stdin.readline
N = int(input())
li=[]
for _ in range(N):
    a, b = map(int, input().split())
    li.append((a,b))
li.append(li[0])
x,y=0,0
for i in range(N):
    x+=li[i][0]*li[i+1][1]
    y+=li[i][1]*li[i+1][0]
print(abs(x-y)/2)