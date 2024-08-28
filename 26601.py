from queue import PriorityQueue
from collections import deque
import math
q = PriorityQueue()
q.put((4,2)) 
N= int(input())
if N==0:
    print(1)
    exit()
def prime_numbers(n):
    arr = [i for i in range(n+1)] # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i*i, n+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0
            
    return [i for i in arr[3:] if arr[i]]
sosu=deque(prime_numbers(2000000))
re=2
for i in range(N-1):
    a,b=q.get()
    c=sosu[0]
    if a>c:
        t=sosu.popleft()
        q.put((t**2,t))
        q.put((a,b))
        re*=t
        re%=2000003
    else:
        q.put((a*a,b))
        re*=a
        re%=2000003
while q.qsize()>0:
    a,b=q.get()
    # print(a,b)
print(re)


# def f(x):
#     g={}
#     while x != 1:
#             for i in range(2, int(math.sqrt(x)) + 1):
#                 if x % i == 0:
#                     x = x // i
#                     if i in g:
#                         g[i] += 1
#                     else:
#                         g[i] = 1
#                     break
#             else:
#                 if x in g:
#                         g[x] += 1
#                 else:
#                         g[x] = 1
#                 break
#     print(g)
#     return g
# f(re)

