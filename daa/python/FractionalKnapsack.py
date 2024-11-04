# Function to solve the Fractional Knapsack problem
def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratio for each item
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    # Sort items by value-to-weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0  # Total value of items in the knapsack
    for ratio, weight, value in items:
        if capacity > 0 and weight <= capacity:
            # Take the whole item
            capacity -= weight
            total_value += value
        else:
            # Take the fraction of the item that fits
            total_value += ratio * capacity
            break  # Knapsack is full

    return total_value

# Input section
try:
    # Number of items
    num_items = int(input("Enter the number of items: "))

    # Weights of items
    weights = list(map(float, input("Enter the weights of items separated by space: ").split()))

    # Values of items
    values = list(map(float, input("Enter the values of items separated by space: ").split()))

    # Capacity of the knapsack
    capacity = float(input("Enter the capacity of the knapsack: "))

    # Validate input lengths
    if len(weights) != num_items or len(values) != num_items:
        raise ValueError("The number of weights and values must match the number of items.")

    # Calculate the maximum value in the knapsack
    max_value = fractional_knapsack(weights, values, capacity)
    print("Maximum value in the knapsack:", max_value)

except ValueError as e:
    print("Invalid input:", e)
