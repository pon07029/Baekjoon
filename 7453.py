import sys
input=sys.stdin.readline
n=int(input())
a=[0]*n
b=[0]*n
c=[0]*n
d=[0]*n
li=[1,2,5,7,8,9]
def findstart(target, li):
    start=0
    end=n-1
    while start <= end:
        mid = (start + end) // 2 
        if li[mid] == target:
            end=mid-1 
        elif li[mid] > target: 
            end = mid - 1
        else:                    
            start = mid + 1
    return  start
def findend(target, li):
    start=0
    end=n-1
    while start <= end:
        mid = (start + end) // 2 
        if li[mid] == target:
            start=mid+1 
        elif li[mid] > target: 
            end = mid - 1
        else:                    
            start = mid + 1
    return end

def ff(aa,bb,cc,lis):
    su=-aa-bb-cc
    return findend(su,lis)
def fff(aa,bb,cc,lis):
    su=-aa-bb-cc
    return findstart(su,lis)


for i in range(n):
    a[i],b[i],c[i],d[i]=map(int,input().split())
a.sort()
b.sort()
c.sort()
d.sort()
result=0
st= fff(b[-1],c[-1],d[-1],a)
end=ff(b[0],c[0],d[0],a)
# print(st,end)
for i in range(st,end+1):
    st1 = fff(a[i],c[-1],d[-1],b)
    end1=ff(a[i],c[0],d[0],b)
    # print(st1,end1)
    for j in range(st1,end1+1):
        st2 = fff(a[i],b[j],d[-1],c)
        end2=ff(a[i],b[j],d[0],c)
        # print(st2,end2+1)
        for k in range(st2,end2+1):
            st3 = fff(a[i],b[j],c[k],d)
            print(st3)
            for i in range(st3,n):
                if a[i]+b[j]+c[k]+d[i]>0:
                    break
                if  a[i]+b[j]+c[k]+d[i]==0:
                    print(a[i],b[j],c[k],d[i])
                    result+=1
                
print(result)