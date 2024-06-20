# ERROR HANDLING
#Basic try-except Block
try:
  result = 10 / 0  
except ZeroDivisionError:
  print("Error: Division by zero!")

# Handling Multiple Exceptions
try:
  file = open('myfile_1.txt', 'r')
except FileNotFoundError:
  print("Error: File not found!")
except IOError:
  print("Error: Input/Output error!")
except Exception as e:
  print("An unexpected error occurred:", e)

# Using else and finally Blocks
try:
  result = 10 / 5
except ZeroDivisionError:
  print("Error: Division by zero!")
else:
  print("Division successful. Result:", result)
finally:
  print("Finally block executed.")

