
import math
def main():
    start = eval(input("Please provide a starting number: "));
    end = eval(input("Please provide a maximum number: "));
    for i in range(start, end):
        if(math.sqrt(i)%1==0):
            print(i);

            
            
