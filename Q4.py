# Program: Student Class with Marks
# creating class student
class Student:
    # constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []   # empty list at start
    
    # method to add a mark
    def add_mark(self, mark):
        try:
            mark = float(mark)   # convert to number
            if mark < 0:
                print("Invalid mark! Cannot be negative.")
            else:
                self.marks_list.append(mark)
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # method to calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    
    # method to display student info
    def display_info(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks List:", self.marks_list)
        print("Average Marks:", round(self.get_average(), 2))

# --- main program ---
# create one student object
name = input("Enter student name: ")
roll = input("Enter roll number: ")
student1 = Student(name, roll)

# add marks using user input
for i in range(5):
    mark_input = input("Enter marks for subject " + str(i+1) + ": ")
    student1.add_mark(mark_input)

# show all details
student1.display_info()
