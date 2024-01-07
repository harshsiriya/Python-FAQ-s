n = int(input("Enter a number : "))
print("Before reversing a number : ", n)
reverse = 0
while n!= 0:
    reverse = reverse *10 + n%10
    n = (n//10)
print("After reversing a number : ", reverse)