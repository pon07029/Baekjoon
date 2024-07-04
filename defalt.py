##############################입력###############################
a = input()
a = int(input())
a= int(sys.stdin.readline())

a, b= map(int, input().split())
a, b = map(int, sys.stdin.readline().split())

dat = list(map(int, input().split()))
dat = list(map(int, sys.stdin.readline().split()))  


data = [input().strip() for i in range(int(input()))]
data = [sys.stdin.readline().strip() for i in range(int(input()))]

import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(b//(a+1))
    except EOFError:
        break


while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break



a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

re=[]
for i in range(int(input())):
  a= int(sys.stdin.readline())
  re.append(a)

##############################출력##############################

print(*li)
print(*re, sep="\n")

li = [0 for i in range(26)]

for i in range(int(input()),0,-1):
    print(i)


if a == "011":
    print("")
elif a == "016":
    print("")
elif a == "019":
    print("")
else:
    print("")


''.join([i * n for i in my_string])

string.count(str(i))



###################################정렬###########################

re = sorted(re, key=len)
re = sorted(re, reverse = True)

data.sort(key=lambda x : int(x[0]))
data.sort(key=lambda x : (x[0], x[1]))

# 딕셔너리의 값들만 추출
values = list(dic.values())


##############################딕셔너리##############################
dat.count(a)
for key, value in dic.items():
    print(f'{key}\n'*value, end="")



#################################기타함수####################################

def binary_search(target, data):
    data.sort()
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
    return


def sosu(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res


  li[a-1], li[b-1] = li[b-1], li[a-1]


def lcm(a, b):
    return a * b / math.gcd(a, b)

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a