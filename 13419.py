for i in range(int(input())):
    s=input()
    l=len(s)
    l1=[]
    l2=[]
    st=0
    while True:
        if st>=l:
            st-=l
        if st>=l:
            st-=l
        if st>=l:
            st-=l
        l1.append(s[st])
        st+=2
      
        if len(l1)>1 and l1[0]==l1[-1]:
            l1.pop(-1)
            break
    st=1
    while True:
        if st>=l:
            st-=l
        if st>=l:
            st-=l
        if st>=l:
            st-=l
        l2.append(s[st])
        st+=2
        if len(l2)>1 and l2[0]==l2[-1]:
            l2.pop(-1)
            break
    print("".join(l1))
    print("".join(l2))