first, second = 0,1
n = int(input("Enter a number for fibonacci series : "))
print("Fibonacci series are ")
for i in range(0,n):
    if i<1:
        result = i
    else:
        result = first+second
        first = second
        second = result
    print(result)