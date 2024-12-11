n=int(input("Enter the Number: "))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("*",end=' ')
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print('*',end=" ")
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(" ",end='')
#     for k in range(i+1):
#         print("*",end='')
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("*",end=' ')
#     print()
# for i in range(n):
#     for k in range((n-1)-i):
#         print("*",end=' ')
#     print()

for i in range(1,n+1):
    for j in range(i):
        print(chr(65+i-1),end='')
    print()