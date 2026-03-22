class code1:
    def FindLargestNum(self,arr):
        max=arr[0]
        for i in arr:
            if max<i:
                max=i
        return i
arr=[2,3,455,64,6,7,3234]
result=code1().FindLargestNum(arr)
print(result)
