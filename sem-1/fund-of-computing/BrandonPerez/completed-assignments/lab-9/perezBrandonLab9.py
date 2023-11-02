#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 10/27/2023
#Description: This is Lab 9. It lists prime and composite numbers from 2-x
#Status: Runs as expected.

import math;
def main():
    
    #prompt for x with error handling while loop
    x = int(input("\nPlease input an integer >=2: "));
    while x < 2:
        x = int(input("\nThat was not a valid input. \nPlease input an integer >=2: "));

    print(f'\nThis program generates and displays list of all prime and composite numbers between 2 and {x}\n'); #formatting
        
    primes = [];
    composites = [];

    for i in range(2, x+1): #iterate all numbers 2 through x (inclusive)
        
        for j in range(2, int(math.sqrt(i)+1)): #iterate all numbers 2 through int(sqrt(i)) (inclusive)
            if not i%j:
                composites.append(i);
                break;
                #if divisible by anything, i is composite
                
        if i not in composites: #if i is not composite, i is prime
            primes.append(i);

    print(f'List of Prime Numbers: \n{str(primes)[1:-1]}\n');
    print(f'List of Composite Numbers: \n{str(composites)[1:-1]}' if x>3 else f'No composite numbers between 2 and {x}');
    #just removing the brackets aka the first and last indeces
        
