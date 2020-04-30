from nssperson import NSSPerson

class Student(NSSPerson):
  
    def __init__(self, id, fname, lname, slack, cohort):
        super().__init__(id, fname, lname, slack)
        self.cohort = cohort
        self.exercises = list()
        
    def student_summary(self):
        print(f"----- STUDENT SUMMARY -----")
        print(f"{self.fname} {self.lname}")
        #TODO: How to know what cohort they're in...
        print(f"Slack Handle: {self.slack}")
        print(f"Exercises Assigned:")
        for exercise in self.exercises:
            print(f"  - {exercise.name}")
        
    def __repr__(self):
        return f"{self.fname} {self.lname} is in {self.cohort}"