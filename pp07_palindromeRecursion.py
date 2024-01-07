n = int(input("Enter a number :"))
def reverse(num):
    if num<10:
        return num
    else:
        return int(str(num%10) + str(reverse(num//10)))
def ispalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if ispalindrome(n) == 1:
    print("Given number is palindrome number")
else:
    print("Given number is not a plaindrome number")