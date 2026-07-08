class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    # ---------------- Students ----------------
    def add_student(self, student):
        self.students[student.get_id()] = student

    def search_student(self, keyword):
            results = []
            for student in self.students.values():
                if keyword.lower() in student.get_id().lower() or keyword.lower() in student.get_name().lower():
                    results.append(student)
            return results

    def update_student(self, student_id, name=None, email=None):

        if student_id not in self.students:
            print("Student not found")
            return

        student = self.students[student_id]

        if name:
            student._Student__name = name 
        if email:
            student.set_email(email)

        print("Student updated successfully")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

        self.grades.pop(student_id, None)

        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)

# ---------------- Courses ----------------
    def add_course(self, course):
        self.courses[course.course_code] = course
    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            self.students[student_id].enroll_course(course_code)
            self.courses[course_code].add_student(student_id)

    # ---------------- Assessments ----------------
    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)

    # ---------------- Grades ----------------
    def record_grade(self, student_id, course_code, title, score):

        if student_id not in self.students:
            print("Student not found")
            return

        if course_code not in self.courses:
            print("Course not found")
            return

        assessment = self.courses[course_code].find_assessment(title)

        if assessment is None:
            print("Assessment not found")
            return

        if score < 0 or score > assessment.max_score:
            print("Invalid score")
            return

        self.grades.setdefault(student_id, {})
        self.grades[student_id].setdefault(course_code, {})

        self.grades[student_id][course_code][title] = score

        print("Grade recorded successfully")

    # ---------------- Average ----------------
    def calculate_average(self, student_id, course_code):

        data = self.grades.get(student_id, {}).get(course_code, {})
        if not data:
            return 0

        percentages = []
        course = self.courses[course_code]

        for title, score in data.items():
            assessment = course.find_assessment(title)
            if assessment:
                percentages.append(assessment.calculate_percentage(score))

        if not percentages:
            return 0

        return sum(percentages) / len(percentages)

    # ---------------- Result ----------------
    def get_result(self, avg):
        return "Passed" if avg >= self.passing_grade else "Failed"

    # ---------------- Letter Grade ----------------
    def get_letter_grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 55:
            return "D"
        else:
            return "F"

    # ---------------- Rankings (CREATIVE FEATURE) ----------------
    def get_student_rankings(self, course_code):

        rankings = []

        for student_id in self.students:
            avg = self.calculate_average(student_id, course_code)
            rankings.append((student_id, avg))

        rankings.sort(key=lambda x: x[1], reverse=True)

        return rankings

    # ---------------- Report ----------------
    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found")
            return

        student = self.students[student_id]

        print("\n===== STUDENT REPORT =====")
        student.display_info()

        if student_id not in self.grades:
            print("No grades available")
            return

        for course_code in self.grades[student_id]:

            course = self.courses[course_code]
            data = self.grades[student_id][course_code]

            print(f"\n===== Course: {course_code} - {course.course_name} =====")

            # Show each assessment breakdown
            for title, score in data.items():
                assessment = course.find_assessment(title)

                if assessment:
                    percent = assessment.calculate_percentage(score)
                    print(f"{title}: {score}/{assessment.max_score} = {percent:.2f}%")
                else:
                    print(f"{title}: {score} (no assessment found)")

            # Calculate average
            avg = self.calculate_average(student_id, course_code)
            result = self.get_result(avg)
            letter = self.get_letter_grade(avg)

            print(f"\nAverage: {avg:.2f}%")
            print(f"Result: {result}")
            print(f"Letter Grade: {letter}")