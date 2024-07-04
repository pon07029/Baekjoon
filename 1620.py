import sys

def binary_search(target, data):

    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid][0] == target:
            return mid 		# target 위치 반환

        elif data[mid][0]  > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return

a, b = map(int, sys.stdin.readline().split())
li = []
li2 = []
le =[]

for i in range(a):
    k=sys.stdin.readline().replace('\n', '')
    li.append(k)
    li2.append([k, i+1])
    
for i in range(b):
    le.append(sys.stdin.readline().replace('\n', ''))

li2.sort(key=lambda x:x[0].lower())
    
for i in le:
    if i.isdigit():
        print(li[int(i)-1])
    else:
        print(li2[binary_search(i,li2)][1])
