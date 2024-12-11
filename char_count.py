a=input("Enter the Word: ")
b=input("Enter the letter to get count: ")
c=list(a)
f=0
for i in c:
    if i==b:
        f=f+1
print(f)