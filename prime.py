num=int(input("Enter the number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("The Number is not Prime ")
            break
        else:
            print("The Number is Prime")
            break
else:
    print("The Number is not Prime")