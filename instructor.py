
class Instructor:
  
    def __init__(self, fname, lname, cohortId, slack):
        self.fname = fname
        self.lname = lname
        self.cohortId = cohortId
        self.slack = slack
        self.specialtiy = ""
        
    def assign_exercise(self, exercise):
      # TODO: 