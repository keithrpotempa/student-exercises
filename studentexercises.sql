CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Slack TEXT NOT NULL,
	CohortId INTEGER NOT NULL,
	FOREIGN KEY (CohortId) 
		REFERENCES Cohort (Id)
);

CREATE TABLE Instructor (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Slack TEXT NOT NULL,
	Specialty TEXT NOT NULL,
	CohortId INTEGER NOT NULL,
	FOREIGN KEY(CohortId) 
		REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL,
	Lang TEXT NOT NULL
);

CREATE TABLE StudentExercises (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ExerciseId INTEGER NOT NULL,
	StudentId INTEGER NOT NULL,
	FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id),
	FOREIGN KEY(StudentId) REFERENCES Student(Id)
)

INSERT INTO Cohort (Name)
VALUES 
	("C38"),
	("C37"),
	("C36");

INSERT INTO Exercise (Name, Lang)
VALUES 
	("Student Exercises", "Python"),
	("Floral Arrangements", "Python"),
	("Coins to Cash", "Python"),
	("Daily Journal", "JavaScript"),
	("Kennel", "React");

SELECT * FROM Instructor;

INSERT INTO Instructor (FirstName, LastName, Slack, Specialty, CohortId)
VALUES
	("Jisie", "David", "jisiedavid", "Python", 1),
	("Andy", "Collins", "andycollins", "Python", 2),
	("Kristen", "Norris", "kristennorris", "C#", 3);

INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES
	("Dar", "Poeta", "darpoeta", 1),
	("Alice", "Quota", "alicequota", 2),
	("Ricky", "Ness", "rickyness", 3),
	("Tess", "Arven", "tessarven", 1),
	("Mickey", "Doff", "mickeydoff", 2),
	("Dag", "Degger", "dagdegger", 3),
	("Stuck", "Here", "stuckhere", 1);
	
SELECT * FROM StudentExercises;

INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES
	(1, 1),
	(2, 1),
	(1, 2),
	(2, 2),
	(1, 3),
	(2, 3),
	(3, 3),
	(1, 4),
	(2, 4),
	(3, 4),
	(1, 5),
	(2, 5),
	(1, 6),
	(2, 6),
	(1, 7),
	(2, 7);
