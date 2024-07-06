import sys
li =[]
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort(key=lambda x : (x[1], x[0]))

end =-1
re =0
for i in li:
    if i[0] >= end:
        re+=1
        end = i[1]
print(re)