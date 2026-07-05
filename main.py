from student import Student
from course import Course
from gradebook import Gradebook

gb = Gradebook()

while True:
    print("\n1. Add Student")
    print("2. Add Course")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        email = input("Email: ")
        gb.add_student(Student(sid, name, email))

    elif choice == "2":
        code = input("Code: ")
        name = input("Name: ")
        gb.add_course(Course(code, name))

    elif choice == "0":
        break