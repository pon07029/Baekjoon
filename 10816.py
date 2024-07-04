a = int(input())
dat = list(map(int, input().split()))
b = int(input())
fi = list(map(int, input().split()))
dat.sort()
aa =list(set(dat))
aa.sort()
bb= []




tmp =0
for i in range(0, len(dat)):
  tmp +=1
  if i == len(dat)-1:
    bb.append(tmp)
    break
  if dat[i] != dat[i+1]:
    bb.append(tmp)
    tmp=0
bb.append(0)
def bin(target):
    
    start = 0 			# 맨 처음 위치
    end = len(aa) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if aa[mid] == target:
            return mid 		# target 위치 반환

        elif aa[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return -1

for i in fi:
  print(bb[bin(i)], end = " ")