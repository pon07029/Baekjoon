import sys
re=[]
for i in range(int(input())):
  a= int(sys.stdin.readline())
  re.append(a)
re.sort()
print(*re, sep="\n")