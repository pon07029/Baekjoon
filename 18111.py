import sys
a, b, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(a):
    dat = list(map(int, sys.stdin.readline().split()))
    for i in dat:
        arr.append(i)
minn = min(arr)
maxx = max(arr)
re =[]
for i in range(minn, maxx+1):
    d= 0
    p= 0
    for j in arr:
        k = i - j
        if k>0:
            p+=k
        else:
            d+=-k
    if c+d >= p :
        re.append([i, p+2*d])
re.sort(key=lambda x: (x[1], -x[0]))
# print(*re)
print(re[0][1], re[0][0])