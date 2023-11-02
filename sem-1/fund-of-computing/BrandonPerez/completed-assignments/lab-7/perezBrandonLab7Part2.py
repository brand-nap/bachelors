#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 10/13/2023
#Description: This is Part 2 of Lab 7. Calculates discounts based on how much is purchased.
#Status: Runs as expected.

def main():
    #Prompts user for quantity and confirms that quantity is a nonnegative number value
    quantity = input("Enter how many packages you would like to purchase: ");
    if quantity.isnumeric():
        quantity = int(quantity);
        if quantity < 0:
            print("Quantity must be numeric and positive");
            return;
    else:
        print("Quantity must be numeric and positive");
        return;

    #each index represents the discount associated with a quantity of 0-9 + 10*n
    discounts = [0,.2,.3,.3,.3,.4,.4,.4,.4,.4];
    
    #Calculate values using my list from earlier
    discPerc = (discounts[ int(quantity / 10) ] if quantity < 100 else .5); #List handles 0-99; Ternary handles all cases above 99
    saved = quantity * 99 * discPerc;
    total = quantity * 99 - saved;

    #Prints out my stuff
    print(f"Discount Percentage is {discPerc*100:.2f}%\nDiscount Amount is ${saved:.2f}\nTotal is ${total:.2f}");
    
    
    
