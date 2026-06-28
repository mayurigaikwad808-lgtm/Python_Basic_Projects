# Program: Student Database using Dictionary
# function of student_database
def student_database():
    students = {}   # dictionary to store student records
    
    while True:
        # show menu
        print("\n--- Student Database Menu ---")
        print("1. Add student")
        print("2. Search student by roll number")
        print("3. Display all students")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        # 1. Add student
        if choice == "1":
            try:
                roll = input("Enter roll number: ")
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                city = input("Enter city: ")
                
                # store record in dictionary
                students[roll] = {"name": name, "age": age, "city": city}
                print("Student added successfully!")
            except ValueError:
                print("Invalid input! Age must be a number.")
        
        # 2. Search student
        elif choice == "2":
            roll = input("Enter roll number to search: ")
            student = students.get(roll)   # use get() to avoid error
            if student:
                print("Student found:", student)
            else:
                print("No student found with this roll number.")
        
        # 3. Display all students
        elif choice == "3":
            if len(students) == 0:
                print("No records available.")
            else:
                print("\nAll Students:")
                for roll, details in students.items():
                    print("Roll:", roll, "Details:", details)
        
        # 4. Exit
        elif choice == "4":
            print("Exiting Student Database. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1-4.")

# call the function
student_database()
