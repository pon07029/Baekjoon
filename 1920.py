import sys

a = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
b = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

def binary_search(target):
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return 1 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return 0

for i in data2:
  print(binary_search(i))
