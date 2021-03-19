n,m=map(int,input().split())
a=[0]*(n+1)
temp=mval=0

for _ in range(m):
    f,l,val=map(int, input().split())
    a[f-1]+=val
    if(l<=n):
        a[l]-=val

for i in a:
    temp+=i
    if(mval<temp):
        mval=temp

print(mval)
