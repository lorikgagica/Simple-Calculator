# Simple Calculator

# Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operation
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 != 0 else "Cannot divide by zero"

# Step 3: Display the results
print("\n--- Calculator Results ----")
print(f"Addition:{number1} + {number2} = {addition}")
print(f"Subtraction:{number1} - {number2} =  {subtraction}")
print(f"Multiplication:{number1} x {number2} =  {multiplication}")
print(f"Division:{number1} / {number2} =  {division}") 



# -----------------------------------------------



# Simple Calculator with Operation Choice

# Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Step 2: Choose the operation
print("\nChoose the operation you want to perform:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (x)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (^)")

choice = input("Enter the number for your choice (1-6): ")

# Step 3: Perform the selected operation
print("\n--- Calculator Result ---")

if choice == "1":
    result = number1 + number2
    print(f"Addition: {number1} + {number2} = {result}")
elif choice == "2":
    result = number1 - number2
    print(f"Subtraction: {number1} - {number2} = {result}")
elif choice == "3":
    result = number1 * number2
    print(f"Multiplication: {number1} x {number2} = {result}")
elif choice == "4":
    if number2 != 0:
        result = number1 / number2
        print(f"Division: {number1} / {number2} = {result}")
    else:
        print("Cannot divide by zero")
elif choice == "5":
    if number2 != 0:
        result = number1 % number2
        print(f"Modulus: {number1} % {number2} = {result}")
    else:
        print("Cannot use modulus with zero")
elif choice == "6":
    result = number1 ** number2
    print(f"Exponentiation: {number1} ^ {number2} = {result}")
else:
    print("Invalid choice. Please enter a number between 1 and 6.")