# Simple Calculator Program
# Performs addition, subtraction, multiplication, or division based on user input.

# Step 1: Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Step 2: Perform the calculation
result = None  # Initialize result variable

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation! Please use +, -, *, or /.")

# Step 3: Display the result (if valid)
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")
