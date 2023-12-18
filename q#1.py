result_list = []

# Iterate through the range of numbers from 2000 to 3200 (both included)
for num in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        # If the conditions are satisfied, add the number to the list
        result_list.append(str(num))

print(result_list)
