a=[-2,-9,31,4,-21,-7]
max1,max2=0,0
if(a[0]>a[1]):
    max1=a[0]
    max2=a[1]
else:
    max1=a[1]
    max2=a[0]
for i in range(2,len(a)-1):
    if(a[i]>max1):
        max2=max1
        max1=a[i]
    elif(a[i]!=max1 and a[i]>max2):
        max2=a[i]
print(max1,max2)