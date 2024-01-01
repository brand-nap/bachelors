
def main():
    while True:
        try:
            length = int(input('Rectangle Length: '));
            width = int(input('Rectangle Width: '));
            print();
            
            rectangle = Rectangle(length, width);
            rectangle.print_rectangle();
            break
        except ValueError:
            print('Invalid input. Please enter an integer\n')
            
        except Exception as e:
            print(f'Unexpected Error: {e}');
            break    

class Rectangle:

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    # returns area
    def get_area(self):
        return self.length*self.width

    # returns perimeter
    def get_perimeter(self):
        return self.length+self.width

    # returns true if it is a square
    def isSquare(self):
        return self.length==self.width

    # prints the rectangle data
    def print_rectangle(self):
        print(f" - Rectangle Info -\nlength x width: {self.length} x {self.width}\nperimeter: {self.get_perimeter()}\narea: {self.get_area()}\nThis rectangle is {'' if self.isSquare() else 'not '}a square") 

    

