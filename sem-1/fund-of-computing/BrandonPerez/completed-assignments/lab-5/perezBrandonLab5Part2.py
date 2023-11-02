#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 9/29/2023
#Description: This is Part 2 of Lab 5. Finds the area of a triangle given length of all sides (a,b,c)
#Status: Runs as expected.

import math;
def main():
    #I wanted to practice loops and sets. I understand there was a simpler way to solve this problem.
    sides = [];
    sum = 0;
    for i in ["a","b","c"]:
        sides.append(eval(input(f"Length of side {i}: ")));
        sum += sides[len(sides)-1];
    s = sum/2;
    print(f"The area of your triangle is {math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2])):.2f}");
    
