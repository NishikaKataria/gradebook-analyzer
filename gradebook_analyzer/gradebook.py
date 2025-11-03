# GradeBook Analyzer
# Name: Nishika Chaudhary
# Course: B.Tech Data Science (1st Year, Semester 1)

print("Welcome to GradeBook Analyzer!")
print("This program helps you analyze student marks easily.\n")

# Task 1: Menu for data input

def menu():
    print("1. Enter student data manually")
    print("2. Load data from CSV file")
    print("3. Exit")


#Task 2: Data entry or CSV import 

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = float(input(f"Enter marks of {name}: "))
        marks[name] = score
    return marks

def csv_input():
    import csv
    marks = {}
    file = input("Enter CSV file name (with .csv): ")
    try:
        with open(file, 'r') as f:
           reader = csv.reader(f)
           next(reader)  # skip header if present
           for row in reader:
               marks[row[0]] = float(row[1])
    except FileNotFoundError:
        print("File not found. Try again.")
    return marks


# Task 3: Statistical functions

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    if n % 2 == 0:
        return (scores[n//2 - 1] + scores[n//2]) / 2
    else:
        return scores[n//2]
    
def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())


# Task 4: Grade assignment

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades


 # Task 5: Pass / Fail     

def pass_fail(marks):
    passed = [n for n, s in marks.items() if s >= 40]
    failed = [n for n, s in marks.items() if s < 40]
    print(f"\nPassed Students ({len(passed)}): {passed}")
    print(f"Failed Students ({len(failed)}): {failed}")

  
  # Task 6: Display results table

def display_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grades[name]}")

     
 # Main Program Loop   

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
       marks = manual_input()
    elif choice == '2':
       marks = csv_input()
    elif choice == '3':
       print("Exiting program. Thank you!")
       break
    else:
        print("Invalid choice! Try again.")
        continue
    if len(marks) == 0:
       print("No data found.")
       continue

    grades = assign_grades(marks)
    display_table(marks, grades)

    print("\n--- Summary ---")
    print(f"Average Marks: {calculate_average(marks):.2f}")
    print(f"Median Marks: {calculate_median(marks):.2f}")
    print(f"Highest Marks: {find_max_score(marks)}")
    print(f"Lowest Marks: {find_min_score(marks)}")

    pass_fail(marks)

    again = input("\nDo you want to analyze again? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using GradeBook Analyzer!")
        break


     
    

    















    
    

 

