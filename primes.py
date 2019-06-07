a=input()
a=a.split()
a=list(map(int,a))
a1=a[0]
a2=a[1]
for n in range(a1+1,a2):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,"",end="")
