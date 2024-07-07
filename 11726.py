a = input()
re=[]
for i in range(int(a)):
    if i == 0:
        re.append(1)
    elif i == 1:
        re.append(2)
    else:
        re.append((re[i-1]+re[i-2])%10007)
print(re[-1])