import sys
def binary_search(target, data):

    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid][0].lower().replace('.', '') == target.lower().replace('.', ''):
            return mid 		# target 위치 반환

        elif data[mid][0].lower().replace('.', '')  > target.lower().replace('.', ''): # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return 0
li =[]
le=[]
a, b = map(int, sys.stdin.readline().split())
for i in range(a):
    c , d =map(str, sys.stdin.readline().split())
    li.append([c, d])
li.sort(key=lambda x:x[0].lower().replace('.', ''))

for i in range(b):
    le.append(sys.stdin.readline().replace('\n', ''))

for i in le:
    print(li[binary_search(i,li)][1])