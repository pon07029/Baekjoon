N = int(input())
li=list(map(int, input().split()))
a,b=0,N-1
mx = [9999999999999,0,0]                 
while(a<b):
    tot=li[a]+li[b] 
    if abs(tot)==0:     
        print(li[a],li[b])
        exit()    
    if abs(tot)<mx[0]:         
        mx = [abs(tot),li[a],li[b]]
    if tot<0: a+=1 	           
    else: b-=1					
print(*mx[1:])
