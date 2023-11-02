#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 10/13/2023
#Description: This is Part 1 of Lab 7.
#Status: Runs as expected.

def main():
    average = 0;

    #Repeat 3 times
    for i in range(1, 4):
        
        #Prompt for score and confirm value is a positive number.
        score = input(f"Enter test score {i}: ");
        if score.isnumeric():
            if int(score) >=0:
                #Average = Sum/Quantity = Addend/Q + Addend/Q +...
                average += int( score ) /3;
            else:
                print("Test score must be numeric and positive");
                return
        else:
            print("Test score must be numeric and positive");
            return
    
    print(f"Average test score is { average : .3f }");
    #List accounts for groups of 10, 0-100
    letter = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"];
    #Ternary accounts for all values over 100; Yay ternary!
    print(f"Your letter grade is { letter[ int( average /10 )] if average <= 100 else 'Undefined' }");
