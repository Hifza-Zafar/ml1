string = input("Enter a string: ")
letter_count = 0
digit_count = 0

for char in string:
    if char.isalpha():  
        letter_count += 1
    elif char.isdigit(): 
        digit_count += 1
    else:
        print("Invalid input")

print("LETTERS", letter_count)
print("DIGITS", digit_count)
