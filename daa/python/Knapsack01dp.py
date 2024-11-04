# Function to solve the 0-1 Knapsack problem using dynamic programming
def knapsack_01_dp(weights, values, capacity):
    num_items = len(weights)
    # Create a 2D DP array where dp[i][w] represents the maximum value that can be obtained 
    # with the first i items and a knapsack capacity of w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    # Build the DP table
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # If the current item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If the current item cannot be included
                dp[i][w] = dp[i - 1][w]

    # The value at dp[num_items][capacity] is the maximum value for the full capacity
    return dp[num_items][capacity]

# Input section
try:
    # Number of items
    num_items = int(input("Enter the number of items: "))

    # Weights of items
    weights = list(map(int, input("Enter the weights of items separated by space: ").split()))

    # Values of items
    values = list(map(int, input("Enter the values of items separated by space: ").split()))

    # Capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Validate input lengths
    if len(weights) != num_items or len(values) != num_items:
        raise ValueError("The number of weights and values must match the number of items.")

    # Calculate the maximum value in the knapsack
    max_value = knapsack_01_dp(weights, values, capacity)
    print("Maximum value in the knapsack:", max_value)

except ValueError as e:
    print("Invalid input:", e)
