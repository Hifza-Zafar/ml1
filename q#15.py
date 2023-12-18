# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# ​
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

a = input("Enter a digit: ")
a = int(a)
output = a + (a * 11) + (a * 111) + (a * 1111)
print(output)
