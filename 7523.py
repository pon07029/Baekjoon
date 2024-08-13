for i in range(int(input())):
    a,b=map(int,input().split())
    print("Scenario #"+str(i+1)+":\n"+str((b+1-a)*(a+b)//2)+"\n")