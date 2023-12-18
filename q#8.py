str = "without,hello,bag,world"
words = str.split(',')
sorted_words = sorted(words)

output_str = ','.join(sorted_words)
print(sorted_words)
print("output str is :",output_str)

