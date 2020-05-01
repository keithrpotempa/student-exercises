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
            SELECT
                e.Id ExerciseId,
                e.Name,
                s.Id,
                s.FirstName,
                s.LastName
            FROM Exercise e
            JOIN StudentExercise se ON se.ExerciseId = e.Id
            JOIN Student s ON s.Id = se.StudentId
        """
        
        # There is no row_factory for this:
        # we're not making any instances here
        row_factory = None
        
        response = self.get_data(row_factory, query)
        print_results(response)

    def student_workload(self):
        """List the exercises assigned to each student"""
        def print_results(dataset):
            students = dict()
            
            for row in dataset:
                student_name = f"{row[0]} {row[1]}"
                exercise_name = row[2] 
                
                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)
                    
            for student_name, exercises in students.items():
                print(student_name)
                for exercise in exercises:
                    print(f"\t- {exercise}")
                

        query = """
            SELECT
                s.FirstName,
                s.LastName,
                e.name AS ExerciseName
            FROM Exercise e
            JOIN StudentExercise se ON se.ExerciseId = e.Id
            Join Student s ON s.Id = se.StudentId;
        """
        
        row_factory = None
        
        response = self.get_data(row_factory, query)
        print("========== STUDENT WORKLOAD ==========")
        print_results(response)

    def assigned_exercises(self):
        """List all exercises assigned by each instructor"""
        def print_results(dataset):
            instructors = dict()
            
            for row in dataset:
                instructor_name = f"{row[0]} {row[1]}"
                exercise_name = row[3]
                
                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    # Note: this one has an extra if statement 
                    # to make sure not to repeat exercises. 
                    # Likely should have been handled in the SQL query though
                    if exercise_name not in instructors[instructor_name]:
                        instructors[instructor_name].append(exercise_name)
            
            for instructor_name, exercises in instructors.items():
                print(instructor_name)
                for exercise in exercises:
                     print(f"\t- {exercise}")
        
        query = """SELECT 
            i.FirstName,
            i.LastName,
            se.ExerciseId as ExerciseId,
            e.Name as ExerciseName
        FROM Instructor i
        JOIN StudentExercise se ON se.InstructorId = i.Id
        JOIN Exercise e ON se.ExerciseId = e.Id;
        """
        
        row_factory = None
        
        response = self.get_data(row_factory, query)
        print("========== ASSIGNED EXERCISES ==========")
        print_results(response)
        
    def popular_exercises(self):
        """Lists all exercises and the students each is assigned"""
        
        def print_results(dataset):
            exercises = dict()
            
            for row in dataset:
                exercise_name = row[0]
                student_name = f"{row[1]} {row[2]}"
                
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
                    
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f"\t- {student}")
        
        query = """
            SELECT 
                e.Name,
                s.FirstName,
                s.LastName
            FROM Exercise e
            JOIN StudentExercise se ON se.ExerciseId = e.Id
            JOIN Student s ON se.StudentId = s.Id
            ORDER BY e.Id;
        """
        
        row_factory = None
        
        response = self.get_data(row_factory, query)
        print("========== POPULAR EXERCISES ==========")
        print_results(response)

reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_exercises()
# reports.exercises_from_language("JavaScript")
# reports.exercises_from_language("Python")
# reports.exercises_from_language("C#")
# reports.all_instructors()
# reports.students_per_exercise()
# reports.student_workload()
# reports.assigned_exercises()
reports.popular_exercises()