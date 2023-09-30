#This calculator enables the user to perform basic arithmetic operations 

# Define a function for addition
def add(a, b):
    return a + b


# Define a function for subtraction
def subtract(a, b):
    return a - b


# Define a function for multiplication
def multiply(a, b):
    return a * b


# Define a function for division
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

print('****** CALCULATOR ******')

# Take user input for the first number
a = float(input("Enter first number: "))

# Take user input for the second number
b = float(input("Enter second number: "))

# Display the menu for the calculator
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n")

# Take the user's choice as an integer
choice = int(input("Enter your choice: "))

# Commence a loop to enable users to perform calculations until they decide to exit
while choice != 5:
    if choice == 1:
        result = add(a, b)
        print(f"Result: {result}")  # Display the result of addition
    elif choice == 2:
        result = subtract(a, b)
        print(f"Result: {result}")  # Display the result of subtraction
    elif choice == 3:
        result = multiply(a, b)
        print(f"Result: {result}")  # Display the result of multiplication
    elif choice == 4:
        result = divide(a, b)
        print(f"Result: {result}")  # Display the result of division
    else:
        print("Invalid choice. Please enter a valid option.")

    choice = int(input("Enter your choice: "))  # Ask for the next choice

# When the user chooses to exit, display a farewell message
print("Thanks for using calculator! Goodbye")
