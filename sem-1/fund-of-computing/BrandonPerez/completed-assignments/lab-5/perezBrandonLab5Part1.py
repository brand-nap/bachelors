#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 9/29/2023
#Description: This is Part 1 of Lab 5. Finds the hypotenuse of a triangle given an angle and its opposite.
#Status: Runs as expected.

import math
def main():
    height = eval(input("How high is the wall you're climbing: "));
    angle = eval(input("What will be the angle of your ladder in degrees: "))/180*math.pi;
    print(f"Your ladder will need to be {height/math.sin(angle):.2f}ft tall");
                  
def simplified():
    print(f"Your ladder will need to be {eval(input('How high is the wall: '))/math.sin(eval(input('What will be the angle of your ladder in degrees: '))/180*math.pi):.2f}ft tall");
