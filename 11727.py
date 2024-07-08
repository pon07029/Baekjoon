re=[]
for i in range(int(input())):
    if i == 0:
        re.append(1)
    elif i == 1:
        re.append(3)
    else:
        re.append((re[i-1]+re[i-2]*2)%10007)
print(re[-1])