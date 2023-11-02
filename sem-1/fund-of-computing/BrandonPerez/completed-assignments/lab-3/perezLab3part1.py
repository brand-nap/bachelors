#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 9/18/2023
#Description: This is Part 1 of Lab 3. It converts F to C.
#Status: Runs as expected.

def main():

    #asks user for first and last name
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    fahr = eval(input("\nProvide a temperature in Fahrenheit: "))
    cels = (fahr-32)*5/9
    print("Hi", first, last, "\n" + str(fahr), "degrees Fahrenheit is", str(cels), "degrees Celsius.")

    
