from student import Student
from course import Course
from gradebook import Gradebook
from assessments.quiz import Quiz
from assessments.exam import Exam
from assessments.project import Project

gb = Gradebook()

while True:
    print("\n===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Add Assignment")
    print("6. Record Grade")
    print("7. View Student Report")
    print("8. Search Student")
    print("9. Update Student")
    print("10. Delete Student")
    print("11. Show Rankings")
    print("0. Exit")

    choice = input("Choose an option: ")

    # ---------------- Add Student ----------------
    if choice == "1":
        gb.add_student(Student(input("ID: "), input("Name: "), input("Email: ")))

    # ---------------- View Students ----------------
    elif choice == "2":
        if not gb.students:
            print("No students found")
        else:
            for s in gb.students.values():
                s.display_info()
        # ---------------- Add Course ----------------
    elif choice == "3":
        gb.add_course(Course(input("Code: "), input("Name: ")))

    # ---------------- Enroll Student ----------------
    elif choice == "4":
        gb.enroll_student(input("Student ID: "), input("Course Code: "))

   # ---------------- Add Assessment ----------------
    elif choice == "5":
        code = input("Course Code: ")
        title = input("Title: ")

        try:
            max_score = int(input("Max Score: "))
        except ValueError:
            print("Invalid max score")
            continue

        t = input("Type (quiz/exam/project): ").lower()

        if t == "quiz":
            gb.add_assessment(code, Quiz(title, max_score))

        elif t == "exam":
            gb.add_assessment(code, Exam(title, max_score))

        elif t == "project":
            gb.add_assessment(code, Project(title, max_score))

        else:
            print("Invalid assessment type")

    # ---------------- Record Grade ----------------
    elif choice == "6":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        title = input("Assessment Title: ")

        try:
            score = float(input("Score: "))
        except ValueError:
            print("Invalid score")
            continue

        gb.record_grade(
            student_id,
            course_code,
            title,
            score
        )
    # ---------------- View Report ----------------
    elif choice == "7":
        gb.show_report(input("Student ID: "))

  # ---------------- Search ----------------
    elif choice == "8":
        keyword = input("Enter ID or Name: ")
        results = gb.search_student(keyword)

        if results:
            for student in results:
                student.display_info()
        else:
            print("Student not found")
  # ---------------- Update ----------------
    elif choice == "9":
        sid = input("Student ID: ")
        name = input("New Name (leave blank to skip): ")
        email = input("New Email (leave blank to skip): ")

        gb.update_student(
            sid,
            name if name else None,
            email if email else None
        )

       # ---------------- Delete ----------------   
    elif choice == "10":
        sid = input("Student ID: ")
        gb.delete_student(sid)
        print("Student deleted successfully")

    # ---------------- Show Rankings ----------------
    elif choice == "11":
        code = input("Course Code: ")

        rankings = gb.get_student_rankings(code)

        print("\n--- Rankings ---")

        if not rankings:
            print("No rankings available")
        else:
            for i, (sid, avg) in enumerate(rankings, start=1):
                print(f"{i}. {sid} -> {avg:.2f}")
    
    # ---------------- Exit ----------------

    elif choice == "0":
        break
    else:
        print("Invalid menu choice")