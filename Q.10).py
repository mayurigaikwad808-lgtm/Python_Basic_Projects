# Program: Smart Calculator & Data Manager

import math     # for scientific calculations
import random   # for random numbers
import time     # for timestamp

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None

# dictionary to store results with timestamp
history = {}

while True:
    print("\n--- Smart Calculator & Data Manager ---")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. Store Results in Dictionary")
    print("5. View History")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    # 1. Basic Arithmetic
    if choice == "1":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operation (+,-,*,/): ")
            
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = sub(a, b)
            elif op == "*":
                result = mul(a, b)
            elif op == "/":
                result = div(a, b)
            else:
                print("Invalid operation!")
                result = None
            
            if result is not None:
                print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    
    # 2. Scientific Calculations
    elif choice == "2":
        try:
            num = float(input("Enter a number: "))
            print("Square root:", math.sqrt(num))
            print("Power (num^2):", math.pow(num, 2))
            print("Sine:", math.sin(num))
            print("Cosine:", math.cos(num))
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # 3. Generate Random Numbers
    elif choice == "3":
        rand_nums = [random.randint(1, 100) for _ in range(5)]
        print("Random Numbers:", rand_nums)
    
    # 4. Store Results in Dictionary
    elif choice == "4":
        data = input("Enter result/data to store: ")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        history[timestamp] = data
        print("Data stored successfully!")
    
    # 5. View History
    elif choice == "5":
        if len(history) == 0:
            print("No history available.")
        else:
            print("\n--- History ---")
            for t, d in history.items():
                print("Time:", t, "-> Data:", d)
    
    # 6. Exit
    elif choice == "6":
        print("Exiting program... Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1-6.")
