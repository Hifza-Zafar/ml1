# Taking input in comma-separated form
input_str = input("Enter two digits (X,Y) separated by a comma: ")
X, Y = map(int, input_str.split(','))

# Generating and printing the 2-dimensional array without a function
output_array = [[i*j for j in range(Y)] for i in range(X)]
print(output_array)
