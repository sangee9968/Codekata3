s=""
no=int(input())
l1=list(map(int,input().split()))
l1.sort()
for i in range(0,len(l1)):
   s=s+str(l1[i])+" "
print(s.strip())   
