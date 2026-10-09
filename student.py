bacche = []

def add_student():
    name = input("Enter name: ")

    try:
        roll = int(input("Enter roll no: "))
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric values.")
        return

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    bacche.append(student)
    print("Student added successfully!")


def calculate_res():
    if not bacche:
        print("No students found.")
        return

    for b in bacche:
        marks = b["marks"]

        if marks >= 85:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Name:", b["name"])
        print("Roll No:", b["roll"])
        print("Marks:", marks)
        print("Grade:", grade)
        print("-------------------")


def view_student():
    if not bacche:
        print("No students found.")
        return

    for b in bacche:
        print("Name:", b["name"])
        print("Roll No:", b["roll"])
        print("Marks:", b["marks"])
        print("-------------------")


def main():
    while True:
        print("\n1. Add Student")
        print("2. View Student")
        print("3. Calculate Result")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            calculate_res()
        elif choice == "4":
            print("Thank you for using Student Analyzer!")
            break
        else:
            print("Invalid choice. Try again.")


main()