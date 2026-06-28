# Program: Sets + Tuples + Modules
#importing modules
import random   # for random numbers
import math     # for square root

try:
    # Step 1: Take 10 numbers as input and store unique numbers in a set
    numbers_set = set()   # empty set
    for i in range(10):
        num = int(input("Enter number " + str(i+1) + ": "))
        numbers_set.add(num)   # duplicates will be removed automatically
    
    print("\nUnique numbers in set:", numbers_set)
    
    # Step 2: Convert set into tuple
    numbers_tuple = tuple(numbers_set)
    print("Tuple from set:", numbers_tuple)
    
    # Step 3: Pick 3 random numbers from tuple
    if len(numbers_tuple) >= 3:
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random numbers from tuple:", random_numbers)
    else:
        print("Not enough unique numbers to pick 3.")
    
    # Step 4: Square root of sum of tuple elements
    total = sum(numbers_tuple)
    print("Sum of tuple elements:", total)
    print("Square root of sum:", round(math.sqrt(total), 2))

except ValueError:
    print("Invalid input! Please enter only numbers.")
except Exception as e:
    print("An error occurred:", e)
