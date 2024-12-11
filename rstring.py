def fibonacci(n):
    if n == 0:  # Base case: Fibonacci(0) = 0
        return 0
    elif n == 1:  # Base case: Fibonacci(1) = 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example Usage
n = 10
fib_sequence = [fibonacci(i) for i in range(n)]
print(fib_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
