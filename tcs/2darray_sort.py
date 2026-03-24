#n=int(input())
a=[]
aa=[(2,5), (2,3), (1,9),(2,8)]
#for i in range(n):
 #   x,y=map(int,input().split())
  #  a.append((x,y))
aa.sort(key=lambda x:x[0])
#aa.sort()
print(aa)