# Taking input in comma-separated form
binary_input = input("Enter comma-separated 4-digit binary numbers: ")

# Splitting the input into a list of binary numbers
binary_numbers = binary_input.split(',')

divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]

output_str = ','.join(divisible_by_5)
print(output_str)
# Checking for divisibility by 5 and creating a list of divisible numbers
