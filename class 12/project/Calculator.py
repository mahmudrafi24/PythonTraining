import math

# Sum Functions
def add(x, y):
    return x + y

# Subtract Functions
def subtract(x, y):
    return x - y

# Multiply Functions
def multiply(x, y):
    return x * y

# Divide Functions
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"
    
# Square Functions
def square(x):
    return x ** 2

# Cubic Functions
def cube(x):
    return x ** 3

# Factorial Functions
def factorial(x):
    return math.factorial(x)

# Prime Functions
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Checking Even or odd numbers
def analyze_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main function
def main():
    while True:
        print("This is our First Project where we can create a Calculator ")
        print("\nSelect an option:")
        print("1. Analysis of numbers")
        print("2. Adding numbers")
        print("3. Subtracting numbers")
        print("4. Multiplying numbers")
        print("5. Divide numbers")
        print("6. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6): ")
    
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        # Analyze and display information about the first number
            print(f"\nAnalysis for {num1}:")
            print(f"Number is {'Even' if num1 % 2 == 0 else 'Odd'}")
            print(f"Number is {'Prime' if is_prime(int(num1)) else 'Composite'}")
            print(f"Factorial of {num1}: {factorial(int(num1))}")
            print(f"Square of {num1}: {square(num1)}")
            print(f"Cube of {num1}: {cube(num1)}")
            
            # Analyze and Display the information about the second number
            print(f"\nAnalysis for {num2}:")
            print(f"Number is {'Even' if num2 % 2 == 0 else 'Odd'}")
            print(f"Number is {'Prime' if is_prime(int(num2)) else 'Composite'}")
            print(f"Factorial of {num2}: {factorial(int(num2))}")
            print(f"Square of {num2}: {square(num2)}")
            print(f"Cube of {num2}: {cube(num2)}\n")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("\nResults:")
            print(f"Summation of {num1} and {num2}: {add(num1, num2)}\n")
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("\nResults:")
            print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}\n")
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("\nResults:")
            print(f"Multification of {num1} and {num2}: {multiply(num1, num2)}\n")
        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("\nResults:")
            print(f"Divide of {num1} and {num2}: {divide(num1, num2)}\n")
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
if __name__ == "__main__":
    main()
