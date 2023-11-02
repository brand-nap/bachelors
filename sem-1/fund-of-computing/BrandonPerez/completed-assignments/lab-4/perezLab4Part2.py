#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 9/22/2023
#Description: This is Part 2 of Lab 4. It finds the perimeter of a box, necessary trim to build the box, and calculates costs.
#Status: Runs as expected.

import math
def main():
    length = eval(input("please provide the length in inches of your box: "));
    width = eval(input("please provide the width in inches of your box: "));
    
    perimeter = 2*(length + width);
    print(f"\nYour box's perimeter is {perimeter} inches.");
    
    numSegments = math.ceil(perimeter/12);
    print(f"You will need {numSegments} segments to build your box");
    
    cost = numSegments * 1.88;
    print(f"It will cost you ${cost}");

    waste = numSegments*12 - perimeter;
    print(f"You wasted {waste} inches of trim");

    moneyLost = round(waste * 1.88*100)/100;
    print(f"You lost ${moneyLost}");

    
