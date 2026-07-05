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

It simulates a real academic gradebook system where users can:

- Add, view, search, update, and delete students  
- Add courses and enroll students  
- Create assessments (Quiz, Exam, Project)  
- Record grades for students  
- Calculate average grades using percentages  
- Generate detailed student reports  
- Show student rankings per course  

---

## 🚀 Features

### 👨‍🎓 Student Management
- Add, view, search, update, and delete students  
- Encapsulation used for secure data handling  

### 📚 Course Management
- Add courses  
- Enroll students in courses  
- Attach assessments to courses  

### 📝 Assessment System
- Quiz, Exam, and Project support  
- Each type uses method overriding  

### 📊 Grade System
- Record grades safely with validation  
- Convert scores into percentages  
- Determine Pass/Fail results  

### 🏆 Ranking System (Custom Feature)
- Students ranked by performance per course  
- Sorted from highest to lowest average  

### 🅰️ Letter Grade System (Custom Feature)
- Converts numeric averages into:
  - A, B, C, D, F  

---

## ▶️ How to Run the Program

Clone the repository and run:

```bash id="runfinal"
python main.py


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