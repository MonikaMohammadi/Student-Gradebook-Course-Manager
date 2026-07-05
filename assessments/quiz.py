from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        if self.calculate_percentage(score) >= 80:
            return "Great quiz"
        return "Keep practicing"