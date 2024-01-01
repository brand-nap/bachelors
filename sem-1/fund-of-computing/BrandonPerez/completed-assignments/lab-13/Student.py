"""
Name: Brandon Perez
Class: CSCI 1411-006
Due Date: 11/30/23
Description: Lab 13
Status: works as expected
"""

class Student:
    """
    Student class which can keep track of student data:
    name, total credit hours, and total quality points.
    It can also calculate gpa
    """

    def __init__(self, name, hours, qpoints):
        """Initialize name, credit hours, and quality"""
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        """Return student's name"""
        return self.name
    
    def getHours(self):
        """Return total credit hours"""
        return self.hours

    def getQPoints(self):
        """Return total quality points"""
        return self.qpoints
    
    def gpa(self):
        """Calculate and return gpa"""
        return self.qpoints/self.hours

    def add_grade(self, grade_point, cred):
        """Add a new course information (Credit Hours and Quality Points)"""
        self.hours = self.hours + cred
        self.qpoints = self.qpoints + grade_point
        
