# Get list of numbers from user
numbers = input("Enter a list of numbers, separated by spaces: ").split()

# Convert list of strings to list of floats
numbers = [float(num) for num in numbers]

# Calculate average of numbers in list
average = sum(numbers) / len(numbers)

# Print result
print("The average of the numbers is:", average)
