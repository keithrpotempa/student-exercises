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
        
    # FIXME: this method doesn't seem quite right to me, 
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
        
    def students_per_exercise(self):
        """Retrieve all exercises and the students working on each"""
        # Different enough from other reports as to not utilize the report method
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()
        
        db_cursor.execute("""
                select
            e.Id ExerciseId,
            e.Name,
            s.Id,
            s.FirstName,
            s.LastName
        from Exercise e
        join StudentExercise se on se.ExerciseId = e.Id
        join Student s on s.Id = se.StudentId
        """)
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'
            
            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else:
                exercises[exercise_name].append(student_name)
                
        for exercise_name, students in exercises.items():
            print(exercise_name)
            for student in students:
                print(f'\t- {student}')
        

reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_exercises()
# reports.exercises_from_language("JavaScript")
# reports.exercises_from_language("Python")
# reports.exercises_from_language("C#")
# reports.all_instructors()
reports.students_per_exercise()