
import sys
a= int(sys.stdin.readline())
re = [5]*(a+1)
for i in range(a+1):
    if i*i <= a:
        re[i*i] = 1
    else:
        break

for i in range(1,a+1):
    j=1
    if re[a] == 1:
        break
    if re[i] == 1:
        continue
    while j*j <= i:
        re[i] = min(re[i], re[i-j*j]+1)
        if re[i] == 2:
            break
        j+=1
        
print(re[a])