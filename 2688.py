le=[[1,1,1,1,1,1,1,1,1,1,1]]
def f(N):
    for i in range(len(le), N+1):
        le.append([sum(le[i-1][:j+1]) for j in range(10)])

for i in range(int(input())):
    n = int(input())
    if n<len(le):
        print(le[n][-1])
    else:
        f(n)
        print(le[n][-1])


    