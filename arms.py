a,b=input("").split()
a=int(a)
b=int(b)
for i in range(a,b):
     s=0
     temp=i
     while(i!=0):
          r=i%10;
          s=s+r*r*r;
          i//=10;
     if(temp==s):
        print(temp,end=" ")
