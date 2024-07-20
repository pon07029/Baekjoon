li=[0]*(int(input())+1)
for i in list(map(int,input().split())):
    li[i]=li[i-1]+1
print(len(li)-max(li)-1)