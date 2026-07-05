from assessment import Assessment

class Project(Assessment):
    def display_info(self):
        print(f"Project: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percent = self.calculate_percentage(score)

        if percent >= 85:
            return "Excellent project"
        elif percent >= 50:
            return "Project submitted"
        else:
            return "Project needs improvement"