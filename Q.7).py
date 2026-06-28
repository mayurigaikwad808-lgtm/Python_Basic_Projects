# Program: Lambda + range() + Lists

try:
    # lambda function to calculate square
    square = lambda x: x * x
    
    # generate numbers from 1 to 20
    numbers = range(1, 21)
    
    # store squares in a list using lambda
    squares_list = [square(n) for n in numbers]
    print("Squares List:", squares_list)
    
    # print only even squares
    print("Even Squares:")
    for sq in squares_list:
        if sq % 2 == 0:
            print(sq)

except Exception as e:
    print("An error occurred:", e)
