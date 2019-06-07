v=int(input())
ss=0
temp=v
while temp>0:
        d=temp%10
        ss+=d**3
        temp//=10
if v==ss:
        print("yes")
else:
        print("no")
