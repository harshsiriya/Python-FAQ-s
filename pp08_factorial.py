num = int(input("Enter a number for factorial : "))
factorial = 1
if num<0:
    print("Factorial can not be calculated ")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("Factorial is : " , factorial)