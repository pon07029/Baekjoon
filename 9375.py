import sys
re=[]
for i in range(int(input())):
    dic={}
    for j in range(int(input())):
        a, b = map(str, sys.stdin.readline().split())
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=1
    value = list(dic.values())
    sum=1
    for j in value:
        sum*=(j+1)
    re.append(sum-1)

print(*re, sep="\n")