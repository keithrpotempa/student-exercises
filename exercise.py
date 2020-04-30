
class Exercise:
  
    def __init__(self, name, language):
        self.name = name
        self.language = language
        
    def __repr__(self):
        return f"{self.name} is in {self.language}"