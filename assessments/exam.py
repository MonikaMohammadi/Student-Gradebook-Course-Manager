from assessment import Assessment

class Exam(Assessment):
    def display_info(self):
        print(f"Exam: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        if self.calculate_percentage(score) >= 55:
            return "Passed exam"
        return "Failed exam"