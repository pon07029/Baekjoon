import sys
a, b = map(int, sys.stdin.readline().split())
l1 = []
l2 =[]
li = []
for i in range(a):
    l1.append(sys.stdin.readline().replace('\n', ''))
for i in range(b):
    l2.append(sys.stdin.readline().replace('\n', ''))
l2.sort()
def binary_search(target, data):
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return -1

for i in l1:
    k = binary_search(i, l2)
    if k != -1:
        li.append(l2[k])
li.sort()
print(len(li))        
print(*li, sep="\n")
