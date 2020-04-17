from nssperson import NSSPerson

class Instructor(NSSPerson):
  
    def __init__(self, fname, lname, slack):
        super().__init__(fname, lname, slack)
        self.specialtiy = ""
        
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)