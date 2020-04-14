
class Instructor:
  
    def __init__(self, fname, lname, slack):
        self.fname = fname
        self.lname = lname
        self.slack = slack
        self.cohort = ""
        self.specialtiy = ""
        
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)