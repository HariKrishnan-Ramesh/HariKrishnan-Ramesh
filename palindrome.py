num=input("Enter the Number: ")
a=list(num)
b=a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")