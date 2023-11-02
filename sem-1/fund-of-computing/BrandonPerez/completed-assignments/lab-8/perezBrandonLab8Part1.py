# Author: Brandon Perez
# Due Date: 10/20/23
# Class: CSCI 1411-006
#
# Description: This is a simple math quiz program that will generate two
# random numbers between 1 and 10, it will display those
# numbers and ask the user to enter the sum of those numbers.
# If the user answers the question correctly then it will display
# the message that the answer is correct. If the user answers the
# question incorrectly then it will display the message Nope with
# the correct answer.
#
#Status: Works as Expected

def main():
    import random
    number1 = random.randint (1, 10);
    number2 = random.randint (1, 10);
    print ('What is', number1, '+', number2, '?');
    answer = int(input ('? '));

    if answer == number1 + number2:
        print ('Your answer is correct')
    else:
        print ('Nope! The correct answer is', number1 + number2)
    
       
