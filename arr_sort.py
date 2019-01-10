st=""
num=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(0,len(l)):
   st=st+str(l)+" "
#print result   
print(st.strip())   
   
