"""
a=[1, 2, 0, 4, 3, 0, 5, 0]
end=len(a)-1
for i in range(len(a)):
    
    while(a[end]==0):
        end-=1
   
    if(a[i]==0 and end>i):
        a[i],a[end]=a[end],a[i]
        end-=1

print(a)
b=[i for i in a if i!=0]
c=a.count(0)
arr=[1, 2, 0, 4, 3, 0, 5, 0]
for i in range(len(a)-1):
    if(arr[i]==0):
        arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)
arr=[1, 2, 0, 4, 3, 0, 5, 0]
start=0
for i in range(len(arr)-1):
    if(arr[i]!=0):
        arr[start]=arr[i]
        start+=1
for j in range(start,len(arr)):
    arr[i]=0
print(arr)
"""

def pushZerosToEnd( arrr):
    start=0
    for i in range(len(arrr)):
        if(arrr[i]!=0):
            arrr[start]=arrr[i]
            start+=1
    for j in range(start,len(arrr)):
        arrr[j]=0
    return arrr
arrr=[3,4,0,0,4]
print(pushZerosToEnd(arrr))