# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# ​
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

string = input("Enter a string: ")
upper_case_count = 0
lower_case_count = 0
for char in string:
    if char.isupper():  
        upper_case_count += 1
    elif char.islower():  
        lower_case_count += 1
    else:
        print("Invalid Input")
print("UPPER CASE", upper_case_count)
print("LOWER CASE", lower_case_count)
