import sys
a, b = map(int, sys.stdin.readline().split())
dat = list(map(int, sys.stdin.readline().split()))
dat.sort()
def binary_search():
  
    start = 0 			# 맨 처음 위치
    end = len(dat) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2
        if f(mid) < b:
            end = mid - 1
        else:
            start = mid + 1

    return [start, end]




def f(start):
    return sum(dat[start:])-dat[start]*len(dat[start:])



s =binary_search()[0]
nsum= sum(dat[s:])
def nf(l):
    return nsum-(a-s)*l

def bbb(target, start,end):

    while start <= end:
        mid = (start + end) // 2 # 중간값
        if nf(mid) == target:
            return mid 		# target 위치 반환

        elif nf(mid) <= target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return end




re =0
if s ==0:
    re = bbb(b,0,dat[s])
else:
    re = bbb(b,dat[s-1],dat[s])

print(re)