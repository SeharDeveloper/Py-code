import os

# Function to display all students
def display_students(students):
    if not students:
        print("No students available.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Function to add a student to the list
def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {'id': student_id, 'name': name, 'age': age, 'grade': grade}
    students.append(student)
    print("Student added successfully!")

# Function to save students data to a file
def save_students_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student['id']}, {student['name']}, {student['age']}, {student['grade']}\n")

# Function to load students data from a file
def load_students_from_file(filename="students.txt"):
    students = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                student_data = line.strip().split(", ")
                if len(student_data) == 4:
                    student = {'id': student_data[0], 'name': student_data[1], 'age': student_data[2], 'grade': student_data[3]}
                    students.append(student)
    return students

# Function to find a student by ID
def find_student_by_id(students, student_id):
    for student in students:
        if student['id'] == student_id:
            return student
    return None

# Main program
def main():
    students = load_students_from_file()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by ID")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
            save_students_to_file(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            student_id = input("Enter student ID to search: ")
            student = find_student_by_id(students, student_id)
            if student:
                print(f"\nStudent Found: ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            else:
                print("Student not found!")
        elif choice == "4":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
