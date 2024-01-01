
from tkinter import *
from tkinter.filedialog import askopenfilename

def main():
    
    # Selects a File
    print("Please choose the file with names and grades in it: ")
    inputFileName = askopenfilename()
    print("file name is ==> ", inputFileName)

    # Converts the File to a List of Students
    students = processFile(inputFileName)

    # Prints each student
    for student in students:
        student.print_student();



def processFile(fileName):
    
    inFile = open(fileName, "r") # open for read
    
    students = []

    # Turns each line into a Student and adds each to list
    line = inFile.readline()
    while line != "":
        students.append(strToStudent(line))
        line = inFile.readline()
    
    inFile.close() # close file

    return students;



def strToStudent(string):
# converts a string to a Student object
    
    parsed = string.split(',') # Split string into list of strings
    
    name = parsed.pop(0)                        # First string is Name
    age = int(parsed.pop(0))                    # Second string is Age
    grades = [int(grade) for grade in parsed]   # Remaining are grades
    return Student(name, age, grades)           # Return Student with given info
    

class Student:

    # Constructor
    def __init__(self, name, age, grades = None):
        self.name = name
        self.age = age
        self.grades = [] if grades is None else grades

    # Adds individual grades
    def add_grade(self, grade):
        self.grades.append(grade)

    # Prints student info in a legible format
    def print_student(self):
        print(f'\n{self.name} - {self.age} years old:\n{str(self.grades)[1:-1]}');


main()















