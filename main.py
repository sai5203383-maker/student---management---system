def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        print("\n--- Student List ---")

        if not students:
            print("No students found.")

        for i, student in enumerate(students, start=1):
            name, age, course = student.strip().split(",")
            print(f"{i}. Name: {name}, Age: {age}, Course: {course}")

    except:
        print("No student records found.")


def update_student():
    try:
        name_to_update = input("Enter student name to update: ")

        with open("students.txt", "r") as file:
            students = file.readlines()

        updated_students = []
        found = False

        for student in students:
            parts = student.strip().split(",")

            if len(parts) != 3:
                updated_students.append(student)
                continue

            name, age, course = parts

            if name.lower() == name_to_update.lower():
                print("Student found! Enter new details:")

                new_name = input("New name: ")
                new_age = input("New age: ")
                new_course = input("New course: ")

                updated_students.append(f"{new_name},{new_age},{new_course}\n")
                found = True
            else:
                updated_students.append(student)

        with open("students.txt", "w") as file:
            file.writelines(updated_students)

        if found:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    except:
        print("Error during update")


def delete_student():
    try:
        name_to_delete = input("Enter student name to delete: ")

        with open("students.txt", "r") as file:
            students = file.readlines()

        updated_students = []
        found = False

        for student in students:
            name, age, course = student.strip().split(",")

            if name.lower() == name_to_delete.lower():
                found = True
                continue
            else:
                updated_students.append(student)

        with open("students.txt", "w") as file:
            file.writelines(updated_students)

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except:
        print("Error during delete")


def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


# MAIN LOOP (DO NOT TOUCH)
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        update_student()

    elif choice == '4':
        delete_student()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice")