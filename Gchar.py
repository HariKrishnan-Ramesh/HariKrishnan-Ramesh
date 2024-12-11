a=input("Enter the Word: ")
b=input("Enter the Word to serach: ")
c=list(a)
for i in c:
    if i==b:
        d=c.index(i)
print(d)

