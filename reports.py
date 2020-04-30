import sqlite3
from student import Student
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

            for row in response:
                print(row)

    def all_students(self):
        """Retrieve all students with the cohort name"""
        
        row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
        
        query = """
            select s.Id,
                s.FirstName,
                s.LastName,
                s.Slack,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """

        self.report(row_factory, query)
                
    def all_cohorts(self):
        """Retrieve all cohorts"""
        row_factory = lambda cursor, row: Cohort(row[1])
        query = """SELECT * FROM Cohort;"""

        self.report(row_factory, query)
        
    def all_exercises(self):
        """Retrieve all exercises"""
        row_factory = lambda cursor, row: Exercise(row[1], row[2])
        query = """SELECT * FROM Exercise;"""
        
        self.report(row_factory, query)

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()