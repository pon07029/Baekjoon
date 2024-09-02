import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int, input().split()))

def f(st, ed):
    if st==ed:
        return li[st]
    mid=(st+ed)//2
    
    mii=min(li[mid], li[mid+1])
    left=mid
    right=mid+1
    mx=max(f(st, mid), f(mid+1, ed), mii*2)
    while st<left or right<ed:
        if right<ed and (left==st or li[left-1]<li[right+1]):
            right+=1
            mii=min(mii, li[right])
        else:
            left-=1
            mii=min(mii, li[left])
        mx=max(mx, mii*(right-left+1))
    return mx
print(f(0, N-1))