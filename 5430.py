from collections import deque
import sys

def f(AD, arr):
    ad = list(AD)
    ar = deque(eval(arr))
    d =0
    for i in ad:
        if i =="R":
            d = d+1
        else:
            if len(ar) ==0:
                return "error"
            if d%2 == 0:
                ar.popleft()
            else:
                ar.pop()
    return list(ar) if d%2 == 0 else list(reversed(ar))

for _ in range(int(input())):
    AD = input()
    n = sys.stdin.readline()
    arr = sys.stdin.readline()
    print(str(f(AD, arr)).replace(" ",""))
        

