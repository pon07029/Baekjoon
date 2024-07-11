import sys
from collections import deque
st =  sys.stdin.readline().strip()
w = sys.stdin.readline().strip()
li =[]
n=len(w)
last = w[-1]
c=0
for i in st:
    li.append(i)
    c+=1
    if i == last and c>=n:
        if ''.join(li[-n:]) == w:
            for _ in range(n):
                li.pop()
            c-=n
print(''.join(li) if li else "FRULA")