# Program: Unique Words from Sentence

import math   # for power calculation

try:
    # Step 1: Take a sentence as input
    sentence = input("Enter a sentence: ")
    
    # Step 2: Split sentence into words
    words = sentence.split()
    
    # Step 3: Extract unique words using set
    unique_words = set(words)
    print("\nUnique words (unsorted):", unique_words)
    
    # Step 4: Print unique words in sorted order
    sorted_words = sorted(unique_words)
    print("Unique words in sorted order:", sorted_words)
    
    # Step 5: Use math module to raise total unique words to power 2
    total_unique = len(unique_words)
    result = math.pow(total_unique, 2)
    print("Total unique words:", total_unique)
    print("Unique words count raised to power 2:", int(result))

except Exception as e:
    print("An error occurred:", e)
