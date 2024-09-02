import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int, input().split()))

def f(st, ed):
    if st==ed:
        return li[st]*li[st], st, st
    mid=(st+ed)//2
    su=li[mid]+li[mid+1]
    mii=min(li[mid], li[mid+1])
    # mx=max(f(st, mid), f(mid+1, ed), su*mii)
    mx=f(st, mid)
    tmp=f(mid+1, ed)
    if mx[0]<tmp[0]:
        mx=tmp
    left=mid
    right=mid+1
    while True:
        if left==st and right==ed:
            break
        if left==st:
            right+=1
            su+=li[right]
            mii=min(mii, li[right])
        elif right==ed:
            left-=1
            su+=li[left]
            mii=min(mii, li[left])
        elif li[left-1]<li[right+1]:
            right+=1
            su+=li[right]
            mii=min(mii, li[right])
        else:
            left-=1
            su+=li[left]
            mii=min(mii, li[left])
        if mx[0]<su*mii:
            mx=su*mii, left, right
    return mx
re=f(0, N-1)
print(re[0])
print(re[1]+1, re[2]+1)
