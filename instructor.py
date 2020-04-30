from nssperson import NSSPerson

class Instructor(NSSPerson):
  
    def __init__(self, id, fname, lname, slack, cohort):
        super().__init__(id, fname, lname, slack)
        self.cohort = cohort
        self.specialtiy = ""
        
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
        
    def __repr__(self):
        return f"{self.fname} {self.lname} is an instructor of {self.cohort}"