import csv

def display_menu():
    print("Welcome to the Student Management System\n")
    print("1. Add a student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Delete a student")
    print("5. Exit")


def add_student():
    with open('students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        email = input("Enter email address: ")
        writer.writerow([name, roll, email])
        print("Student added successfully!")


def view_students():
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student():
    roll = input("Enter roll number to search: ")
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[1] == roll:
                print("Name: ", row[0])
                print("Roll: ", row[1])
                print("Email: ", row[2])
                found = True
                break
        if not found:
            print("Student not found!")


def delete_student():
    roll = input("Enter roll number to delete: ")
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = []
        found = False
        for row in reader:
            if row[1] == roll:
                found = True
            else:
                rows.append(row)
        if found:
            with open('students.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Student deleted successfully!")
        else:
            print("Student not found!")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if _name_ == "_main_":
    main()
