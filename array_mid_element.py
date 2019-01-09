n=int(input())
l=list(map(int,input().strip().split()))
l.sort()
a=len(l)//2
print(l[a])   
