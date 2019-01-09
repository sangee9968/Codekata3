n,a,d=map(int,input().strip().split())
sum=0
for i in range(1,n+1):
   an=a+(i-1)*d
   sum=sum+an
print(sum)   
