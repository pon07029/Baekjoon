import sys
input=sys.stdin.readline
N=int(input())
s,l="",""
li=[]
for i in range(N):
    li.append(input().strip())
M=int(input())
arr=[]
for i in range(M):
    arr.append(input().strip())
if N==1:
    print(arr[0])
    exit()

for i in range(N):
    
    if li[i]=='?':
        if i==0:
            l=li[i+1][0]
        elif i==N-1:
            s=li[i-1][-1]
        else:
            s=li[i-1][-1]
            l=li[i+1][0]
        break
for i in range(M):
    for j in range(N):
        if arr[i] == li[j]:
            arr[i] = ",,,,,,,,"


if l=="":
    for i in range(M):
        if arr[i][0]==s:
            print(arr[i])
            break
elif s=="":
    for i in range(M):
        if  arr[i][-1]==l:
            print(arr[i])
            break
else:
    for i in range(M):
        if arr[i][0]==s and arr[i][-1]==l:
            print(arr[i])
            break