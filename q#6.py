C = 50
H = 30

def calculate_Q(D):
    return round((2 * C * D / H) ** 0.5)

input_sequence = input("Enter comma-separated values for D: ")
D_values = [int(value) for value in input_sequence.split(',')]
result_values = [calculate_Q(D) for D in D_values]
print(','.join(map(str, result_values)))
