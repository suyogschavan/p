# Iterative approach to calculate Fibonacci numbers
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive approach to calculate Fibonacci numbers
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Optimized recursive approach with memoization to calculate Fibonacci numbers
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Example usage:
n = 10
print("Iterative:", fibonacci_iterative(n))
print("Recursive:", fibonacci_recursive(n))
print("Memoized Recursive:", fibonacci_memoized(n))
