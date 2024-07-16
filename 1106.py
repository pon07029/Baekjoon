C, N =map(int, input().split())
li=[]
for i in range(N):
    a,b = map(int, input().split())
    li.append((a,b))
li.sort(key=lambda x: x[0])
re=[0]
for i in range(1,100000):
    mx=0
    for j, k in li:
        if j >i:
            break
        mx=max(mx, k+re[i-j])
    re.append(mx)
    if mx>=C:
        break
print(len(re)-1)