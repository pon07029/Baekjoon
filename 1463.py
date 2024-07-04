a = int(input())

li= [0 for i in range(a+2)]

for i in range(1, a+1):
    tmp = []
    tmp.append(li[i-1]+1)
    if i%2 == 0:
        tmp.append(li[i//2]+1)
    if i%3 == 0:
        tmp.append(li[i//3]+1)
    li[i] = min(tmp)

print(li[a]-1)