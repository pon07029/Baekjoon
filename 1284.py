li =[]
while True:
    a=input()
    
    if a == "0":
        break
    li.append(len(a)*4+1+a.count("0")-a.count("1"))
print(*li, sep="\n")