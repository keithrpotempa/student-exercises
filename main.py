from cohort import Cohort 
from exercise import Exercise
from instructor import Instructor
from student import Student

exercise1 = Exercise("Exercise 1", "HTML")
exercise2 = Exercise("Exercise 2", "JavaScript")
exercise3 = Exercise("Exercise 3", "React")
exercise4 = Exercise("Exercise 4", "Python")

cohort38 = Cohort("Day Cohort 38")
cohort39 = Cohort("Day Cohort 39")
cohort40 = Cohort("Day Cohort 40")

student1 = Student("Elmer", "Schmidt", "elmerschmidt")
student2 = Student("Kathryn", "McGee", "kathrynmcgee")
student3 = Student("Love", "Grayson", "lovegrayson")
student4 = Student("Taelyn", "Dickens", "taelyndickens")

cohort38.students.append(student1)
cohort39.students.append(student2)
cohort40.students.append(student3)
cohort38.students.append(student4)

instructor1 = Instructor("Jayden", "Massey", "jaydenmassey")
instructor2 = Instructor("Love", "Grayson", "lovegrayson")
instructor3 = Instructor("Anita", "Cruz", "anitacruz")

cohort38.instructors.append(instructor1)
cohort39.instructors.append(instructor2)
cohort40.instructors.append(instructor3)

instructor1.assign_exercise(student1, exercise1)
instructor1.assign_exercise(student1, exercise2)

instructor1.assign_exercise(student2, exercise1)
instructor1.assign_exercise(student2, exercise2)

instructor1.assign_exercise(student3, exercise3)
instructor1.assign_exercise(student3, exercise4)

instructor1.assign_exercise(student4, exercise3)
instructor1.assign_exercise(student4, exercise4)

#Challenge
students = [student1, student2, student3, student4]
exercises = [exercise1, exercise2, exercise3, exercise4]

for student in students:
  student.student_summary()