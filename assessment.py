class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percent = self.calculate_percentage(score)
        if percent >= 50:
            return "Passed"
        return "Failed"

    def display_info(self):
        print("Title:", self.title)
        print("Max Score:", self.max_score)