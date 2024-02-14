# Packages needed:
# pip install math
# pip install time
# pip install datetime

import math
import time
from datetime import datetime

#Normal Calculator functions

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

# Modulus Functions
def modulus(x, y):
    return x % y

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

# BMI Calculator functions

# This function is used to calculate feet,inches to meters
def feet_and_inches_to_meters(feet, inches):
    # Convert feet and inches to meters
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254  # 1 inch = 0.0254 meters
    return meters

# Calculating BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

# Interpretation of the BMI formula
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Age Calculator functions
def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    current_date = datetime.now()
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    days_lived = (current_date - birthdate).days
    months_lived = age * 12 + current_date.month - birthdate.month
    return age, days_lived, months_lived

def main():
    while True:
        print("Hello! This super calculator is made by Team Noob. Hope you will like this! 😊")
        time.sleep(5)
        print("\nSelect an option:")
        print("1. Normal Calculator")
        print("2. BMI Calculator")
        print("3. Age Calculator")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

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
            print(f"Cube of {num2}: {cube(num2)}")
    
            # Perform calculations
            print("\nResults:")
            print(f"Sum: {add(num1, num2)}")
            print(f"Difference: {subtract(num1, num2)}")
            print(f"Multification: {multiply(num1, num2)}")
            print(f"Division: {divide(num1, num2)}")
            print(f"Modulus: {modulus(num1, num2)}")


        elif choice == '2':
            weight = float(input("Enter your weight in kilograms: "))
            unit_choice = input("Enter '1' for meters or '2' for feet and inches: ")

            if unit_choice == '1':
                height_meters = float(input("Enter your height in meters: "))
            elif unit_choice == '2':
                feet = float(input("Enter your height in feet: "))
                inches = float(input("Enter your height in inches: "))
                height_meters = feet_and_inches_to_meters(feet, inches)
            else:
                print("Invalid unit choice. Please enter '1' or '2'.")
                continue

            bmi = calculate_bmi(weight, height_meters)
            interpretation = interpret_bmi(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print(f"Interpretation: {interpretation}\n")

        elif choice == '3':
            birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
            try:
                age, days_lived, months_lived = calculate_age(birthdate_str)
                print(f"You are {age} years old.")
                print(f"You have lived for {days_lived} days.")
                print(f"You have lived for {months_lived} months.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()