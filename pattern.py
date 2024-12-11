# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")---
#     for k in range(i+1):
#         print("*",end="")
#     print()

def array():
    num = [1, 2, 3, 4, 5, 6]
    k = 1
    subarrays = []  # List to store the subarrays

    # Iterate over the indices of the list num
    for i in range(len(num)):
        for j in range(len(num)):
            # Check if the difference between num[i] and num[j] equals k
            if num[i] - num[j] == k:
                # Create a subarray with the two elements
                subarray = [num[j], num[i]]
                # Add the subarray to the list of subarrays
                subarrays.append(subarray)
    
    # Find the subarray with the largest sum
    max_sum = float('-inf')
    max_subarray = []

    for subarray in subarrays:
        current_sum = sum(subarray)
        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray = subarray
    
    # Print the subarray with the largest sum
    print("Subarray with the largest sum:", max_subarray)

array()

