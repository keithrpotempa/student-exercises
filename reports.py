import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/kpotempa/workspace/student-exercises/studentexercises.db"

    def report(self, row_factory, query):
        """ Generic report method"""
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = row_factory
            db_cursor = conn.cursor()
            db_cursor.execute(query)
            response = db_cursor.fetchall()
            
            if len(response) > 0:
              for row in response:
                  print(f"  - {row}")
            else:
              print("   - None")

    def all_students(self):
        """Retrieve all students with the cohort name"""
        
        row_factory = lambda cursor, row: Student(
                row[0], row[1], row[2], row[3], row[5]
            )
        
        query = """
            SELECT s.Id,
                s.FirstName,
                s.LastName,
                s.Slack,
                s.CohortId,
                c.Name
            FROM Student s
            JOIN Cohort c ON s.CohortId = c.Id
            ORDER BY s.CohortId
            """
            
        print(f"All Students:")
        self.report(row_factory, query)
        print("")
                
    def all_cohorts(self):
        """Retrieve all cohorts"""
        row_factory = lambda cursor, row: Cohort(row[1])
        query = """SELECT * FROM Cohort;"""
        
        print(f"All Cohorts:")
        self.report(row_factory, query)
        print("")
        
    def all_exercises(self):
        """Retrieve all exercises"""
        row_factory = lambda cursor, row: Exercise(row[1], row[2])
        query = """SELECT * FROM Exercise;"""
        
        print(f"All Exercises:")
        self.report(row_factory, query)
        print("")
        
    def all_instructors(self):
        """Retrieve all instructors with the cohort name"""
        
        row_factory = lambda cursor, row: Instructor(
                row[0], row[1], row[2], row[3], row[5]
            )
        
        query = """
            SELECT i.Id,
                i.FirstName,
                i.LastName,
                i.Slack,
                i.CohortId,
                c.Name
            FROM Instructor i
            JOIN Cohort c ON i.CohortId = c.Id
            """
            
        print(f"All Instructors:")
        self.report(row_factory, query)
        print("")
        
    # FIXME: The methods from here on down don't seem quite right to me, 
    # considering we've already all the exercise data over to python instances
    # we shouldn't be making duplicate instances...
    def exercises_from_language(self, language):
        """Retrieve all exercises of one language"""
        row_factory = lambda cursor, row: Exercise(row[1], row[2])
        query = f"""
          SELECT * FROM EXERCISE
          WHERE Lang = "{language}";
        """
        
        print(f"Exercises in {language} include:")
        self.report(row_factory, query)
        print("")

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.exercises_from_language("JavaScript")
reports.exercises_from_language("Python")
reports.exercises_from_language("C#")
reports.all_instructors()