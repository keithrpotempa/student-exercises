import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/kpotempa/workspace/student-exercises/studentexercises.db"

    def get_data(self, row_factory, query):
        """ Generic get data method"""
        
        with sqlite3.connect(self.db_path) as conn:
            # This handles situations where we don't need a row_factory
            if row_factory != None:
                conn.row_factory = row_factory
            db_cursor = conn.cursor()
            db_cursor.execute(query)
            response = db_cursor.fetchall()
            
            return response

    def print_report(self, report_title, data):
        print(f"{report_title}")
        if len(data) > 0:
            for row in data:
                print(f"  - {row}")
        else:
            print("   - None")
        print("")

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
            
        response = self.get_data(row_factory, query)
        self.print_report("All Students", response)
                
    def all_cohorts(self):
        """Retrieve all cohorts"""
        row_factory = lambda cursor, row: Cohort(row[1])
        query = """SELECT * FROM Cohort;"""
        
        response = self.get_data(row_factory, query)
        self.print_report("All Cohorts", response)
        
    def all_exercises(self):
        """Retrieve all exercises"""
        row_factory = lambda cursor, row: Exercise(row[1], row[2])
        query = """SELECT * FROM Exercise;"""
        
        response = self.get_data(row_factory, query)
        self.print_report("All Exercises", response)
        
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
            
        response = self.get_data(row_factory, query)
        self.print_report("All Instructors", response)
        
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
        
        response = self.get_data(row_factory, query)
        self.print_report(f"Exercises in {language} include", response)

    def students_per_exercise(self):
        """Retrieve all exercises and the students working on each"""
        def print_results (dataset):
            exercises = dict()
            
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
        
        query = f"""
                select
            e.Id ExerciseId,
            e.Name,
            s.Id,
            s.FirstName,
            s.LastName
        from Exercise e
        join StudentExercise se on se.ExerciseId = e.Id
        join Student s on s.Id = se.StudentId
        """
        
        # There is no row_factory for this:
        # we're not making any instances here
        row_factory = None
        
        response = self.get_data(row_factory, query)
        print_results(response)

reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_exercises()
# reports.exercises_from_language("JavaScript")
# reports.exercises_from_language("Python")
# reports.exercises_from_language("C#")
# reports.all_instructors()
reports.students_per_exercise()