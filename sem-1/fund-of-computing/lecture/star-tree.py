#Brandon Perez
#Star Tree Participation Assignment

def main():
    #completes the assignment as requested
    
    #prompt user for # of layers (int)
    n = int(input("How tall is your star tree: "));

    #loop creates largest string of stars
    stars = "";
    for i in range(n+1):
        stars += "*";

    print(""); #just some formatting
    
    #loop prints decrementing substrings of string stars
    for i in range(n+1):
        print(stars[0:n-i]);
            
            
def universal():
    #can create both decrementing and incrementing star trees given user input

    #prompt user for # of layers (int)
    n = int(input("How tall is your star tree: "));
    
    #prompt user for whether or not stars should increment or decrement & confirm user gave a valid input
    increment = input("Increasing or Decreasing Order (I/D): ")
    while(increment != "I" and increment != "D"):
        increment = input("\nInvalid Input. Please Enter I or D\nIncreasing or Decreasing Order (I/D): ")
    increment = increment=="I";

    #loop creates largest string of stars
    stars = "";
    for i in range(n+1):
        stars += "*";
    
    #loop prints either incrementing or decrementing substrings of string stars
    for i in range(n+1):
        print(stars[0:i if increment else n-i]); #Ternary for the Win!
