# Program: Analyze String
#Function to analyze a string

def analyze_string(s):
    # check if string is empty
    if s == "":
        print("Empty string entered!")
        return
    
    # length of string
    print("Length of string:", len(s))
    
    # reverse string using slicing
    print("Reverse string:", s[::-1])
    
    # count vowels (case insensitive)
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)
    
    # print each character with positive and negative index
    for i in range(len(s)):
        print("Character:", s[i], "Positive index:", i, "Negative index:", i - len(s))

# take input from user
user_input = input("Enter a string: ")
analyze_string(user_input)
