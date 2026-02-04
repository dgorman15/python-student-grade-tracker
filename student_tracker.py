students = {}

def add_student(students):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[name] = grade
    print(f"{name} added with grade {grade}")

def main():
    while True:
        print("\nStudent Grade Tracker")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            print("View students selected")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()