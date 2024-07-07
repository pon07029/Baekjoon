from queue import PriorityQueue
import sys
q = PriorityQueue() 

def fun(a):
    if a==0:
        if q.empty():
            print(0)
        else:
            print(q.get())
    else:
        q.put(a)

for i in range(int(input())):
    a= int(sys.stdin.readline())
    fun(a)