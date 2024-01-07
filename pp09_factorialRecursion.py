def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

num = int(input("Enter a number to find factorial : "))
if num<0:
    print("Factorial cant b calculated")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial is : " , fact(num))