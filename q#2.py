num = int(input("Enter a number: "))
result = 1

# Calculate factorial of entered number
for i in range(1, num + 1):
    result *= i
print("Factorial of a number :",result)
