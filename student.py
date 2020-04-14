
class Student:
  
    def __init__(self, fname, lname, slack):
        self.fname = fname
        self.lname = lname
        self.cohort = ""
        self.slack = slack
        self.exercises = list()
        
    def student_summary(self):
        print(f"----- STUDENT SUMMARY -----")
        print(f"{self.fname} {self.lname}")
        #TODO: How to know what cohort they're in...
        print(f"Slack Handle: {self.slack}")
        print(f"Exercises Assigned:")
        for exercise in self.exercises:
            print(f"  - {exercise.name}")
        