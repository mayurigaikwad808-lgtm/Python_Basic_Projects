# Program: Manage Marks
# function to manage marks
def manage_marks():
    marks = []   # empty list to store marks
    
    # taking 5 subject marks as input
    for i in range(5):
        try:
            mark = float(input("Enter marks of subject " + str(i+1) + ": "))
            marks.append(mark)   # add mark to list
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return   # stop function if wrong input
    
    # printing the list of marks
    print("\nMarks List:", marks)
    
    # calculate average, highest and lowest
    average = sum(marks) / len(marks)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
    
    # sort marks in descending order
    marks.sort(reverse=True)
    print("Marks in Descending Order:", marks)

# call the function
manage_marks()
