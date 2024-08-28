import sys
input=sys.stdin.readline
N= int(input())
li=list(map(int, input().split()))

def prime_numbers(n):
    arr = [i for i in range(n+1)] # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i*i, n+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]
sosu=prime_numbers(li[-1]*2//(N))
re=1
for p in sosu:
    if p*re>li[-1]:
        break
    g={}
    for i in range(N):
        na=li[i]%p
        if na in g:
            g[na]+=1
        else:
            g[na]=1
    re=max(re, max(g.values()))
print(re)