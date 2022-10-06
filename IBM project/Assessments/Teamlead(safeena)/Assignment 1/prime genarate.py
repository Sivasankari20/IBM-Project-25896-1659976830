end=int(input("Enter range:"))
for n in range(1,end):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)
