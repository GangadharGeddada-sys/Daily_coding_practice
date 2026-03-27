def brute():
    a=[16, 17, 4, 3, 5, 2]
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                if(j==len(a)-1):
                    print(a[i])
            else:
                break
        print()
def optimal(a):
    max=float('-inf')
    arr=[]
    for i in range(len(a)-1,-1,-1):
        if(a[i]>=max):
            max=a[i]
            arr.append(a[i])
    arr.sort(reverse=True)
    print(arr)
a=[60,60,56]
optimal(a)
