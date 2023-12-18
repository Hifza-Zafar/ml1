result_numbers = []
for num in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        result_numbers.append(str(num))
result_str = ','.join(result_numbers)
print(result_str)
