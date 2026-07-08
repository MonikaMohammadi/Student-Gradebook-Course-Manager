# 📘 Student Gradebook & Course Manager

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OOP](https://img.shields.io/badge/Object%20Oriented-Programming-orange)
![Status](https://img.shields.io/badge/Project-Completed-green)
![Level](https://img.shields.io/badge/Level-University-lightgrey)

---

## 👤 Author
**Monika Mohammadi**

---

## 🎯 Project Title
### Student Gradebook & Course Manager (Python OOP Project)

---

## 📌 Project Description

This is a **terminal-based Python application** that manages students, courses, assessments, and grades using Object-Oriented Programming (OOP).

The application allows users to:

- Add, view, search, update, and delete students
- Add courses and enroll students
- Create assessments (Quiz, Exam, and Project)
- Record grades for students
- Calculate average grades using percentages
- Generate detailed student reports
- Show student rankings for each course

---

## 🏗️ Classes Created

This project contains the following classes:

- **Student** – Stores student information and enrolled courses.
- **Course** – Stores course details, enrolled students, and assessments.
- **Assessment** – Parent class for all assessments.
- **Quiz** – Child class of Assessment.
- **Exam** – Child class of Assessment.
- **Project** – Child class of Assessment.
- **Gradebook** – Manages students, courses, assessments, grades, reports, and rankings.

---

## 💡 OOP Concepts Used

### 🔒 Encapsulation
Encapsulation is implemented in the **Student** class by using private attributes:

- `__student_id`
- `__name`
- `__email`

These attributes are accessed or modified through the following methods:

- `get_id()`
- `get_name()`
- `set_email()`

---

### 👨‍👩‍👧 Inheritance

The **Assessment** class is the parent class.

The following classes inherit from it:

- **Quiz**
- **Exam**
- **Project**

This allows all assessment types to share common functionality while providing their own behaviors.

---

### 🔄 Method Overriding

The child classes **Quiz**, **Exam**, and **Project** override the following methods inherited from the **Assessment** class:

- `display_info()`
- `grade_message()`

Each class displays assessment-specific information and provides customized grading feedback.

---

## 🚀 Features

### 👨‍🎓 Student Management
- Add students
- View students
- Search students
- Update student information
- Delete students

### 📚 Course Management
- Add courses
- Enroll students in courses
- Attach assessments to courses

### 📝 Assessment Management
- Create Quiz assessments
- Create Exam assessments
- Create Project assessments

### 📊 Grade Management
- Record grades
- Validate entered scores
- Calculate percentage averages
- Display Pass/Fail results
- Generate student reports

---

## ⭐ Custom Features

### 🏆 Ranking System
Displays students ranked from the highest average score to the lowest average score for each course.

### 🅰️ Letter Grade System
Converts percentage averages into letter grades:

- A
- B
- C
- D
- F

---

## ▶️ How to Run the Program

Clone the repository and run:

```bash
python main.py
```

---

## 📁 Project Structure

```text
project/
│── main.py
│── student.py
│── course.py
│── gradebook.py
│
└── assessments/
    │── assessment.py
    │── quiz.py
    │── exam.py
    │── project.py
```

---

## 🎯 Project Objectives

This project demonstrates:

- Python programming fundamentals
- Object-Oriented Programming (OOP)
- Classes and Objects
- Encapsulation
- Inheritance
- Method Overriding
- Lists and Dictionaries
- Input Validation
- Terminal-based application development

