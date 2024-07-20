N =int(input())
dat = list(map(int, input().split()))
# g={}
# for i in range(1,len(dat)):
#     if dat[i] in g:
#         g[dat[i]].append(i)
#     else:
#         g[dat[i]] = [i]
li=[[]]
for i in range(1,N):
    li.append([])
    li[dat[i]].append(i)

def f(p):
    if not li[p]:
        return 0
    tmp = [f(i) for i in li[p]]
    tmp.sort(reverse=True)
    for i in range(len(tmp)):
        tmp[i]+=i
    return max(tmp)+1
print(f(0))