#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 10/6/2023
#Description: This is Part 1 of Lab 6.
#Status: Runs as expected.

def main():
    first = input("First name: ").lower();
    last = input("Last name: ").lower();
    print(f"\nYour username  :  {last + first[0]}");
    print(f"Your University of Colorado Denver email  :  {first}.{last}@ucdenver.edu");
