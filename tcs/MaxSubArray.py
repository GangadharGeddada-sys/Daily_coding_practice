a=[2,3,-3,4,-5,-3]
msum=a[0]
sum=a[0]
start=0
end=0
for i in range(1,len(a)):
    if(sum>=0):
        sum+=a[i]
    else:
        sum=a[i]
        start=0
    print(sum)
    if(sum>msum):
        msum=sum
        end=i
print(end)
