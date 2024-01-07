i,temp = 0,0
n = int(input("Enter a number : "))
for i in range(2,n//2):
    if n%i == 0:
        temp = 1
        break
if temp == 1:
    print("Given number is not a prime number")
else:
    print("Given number is prime number")

