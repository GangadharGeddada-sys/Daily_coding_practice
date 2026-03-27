class hello():
    def rotateOwn(self,arr,k):
        while(k>0):
            n=arr[0]
            arr.remove(n)
            arr.append(n)
            k-=1
    def rotateOne(self,arr):
        temp=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[len(arr)-1]=temp
    def rotateArray(self,arr,k):
        k=k%len(arr)
        print(k)
        if(k<0):
            k=k+len(arr)
        for i in range(k):
            self.rotateOne(arr)
    def  reversearray(self,arr,start,end):
        while(start<end):
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
    def rotateByReverse(self,arr,k):
        k=k%len(arr)
        if(k<0):
            k=k+len(arr)
        self.reversearray(arr,0,k-1)
        self.reversearray(arr,k,len(arr)-1)
        arr.reverse()
        return arr
    def pri(self):
        a=[1,2,3,4,5]
        k=2   
        #self.rotateArray(a,k)
        #self.rotateByReverse(a,k)
        self.rotateOwn(a,k)
        return a
aa=hello()
print(aa.pri())