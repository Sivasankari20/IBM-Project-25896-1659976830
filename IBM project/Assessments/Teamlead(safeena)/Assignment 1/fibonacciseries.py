n=int(input("Enter the range:"))
fib1=0
fib2=1
print(fib1)
print(fib2)
for i in range(n):
    fib3=fib1+fib2
    print(fib3)
    fib1=fib2
    fib2=fib3
    
