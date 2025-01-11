def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if len(numeric_numbers) != len(numbers):
        raise ValueError("List contains non-numeric values.")
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1,2,3,4,'a']
#This will raise ValueError
try:
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")
