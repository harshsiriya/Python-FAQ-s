first, second = 0,1
n = int(input("Enter a number for fibonacci series : "))
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("Fibonacci series is : ")
for i in range(0,n):
    print(fibonacci(i))