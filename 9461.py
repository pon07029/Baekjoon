re = [1,1,1,2,2,3,4,5,7,9]
li = []
for i in range(int(input())):
    a= int(input())
    li.append(a)
if max(li) > 9:
    for i in range(10, max(li)):
        re.append(re[i-2]+re[i-3])

for i in li:
    print(re[i-1])