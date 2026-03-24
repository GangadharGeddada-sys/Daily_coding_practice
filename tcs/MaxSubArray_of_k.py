#sliding window
a=[-2,-9,-31,-4,-21,-7]
k=3
#for i in range(len(a)-k+1):
#    sum=0
#   for j in range(i,i+k):
#        sum+=a[j]
#   print(sum)
wsum=0
msum=float('-inf')
for i in range(k):
    wsum+=a[i]
for j in range(k,len(a)):
    wsum=wsum-a[j-k]+a[j]
    msum=max(wsum,msum)
print(msum)