#Brandon Perez
#Class: CSCI 1411-006
#Due Date: 10/6/2023
#Description: This is Part 2 of Lab 6. Asks for purchase information of an item and prints a bill.
#Status: Runs as expected.

def main():
    #Inputting Stuff
    itemName = input("Enter item name: ");
    quantity = int(input("Enter quantity of item: "));
    price = eval(input("Enter the Price of the item: "));
    taxRate = eval(input("Enter the sales tax rate: "));

    #Printing the values we just inputted
    print(f"Item name: {itemName}");
    print(f"Quantity: {quantity}");
    print(f"Price: ${price:.2f}");

    #Calculating remaining values given user input
    subtotal = price*quantity;
    tax = subtotal*taxRate/100;
    total = subtotal+tax;

    #Printing remainder variables that we just calculated
    print(f"Total amount: ${subtotal:.2f}");
    print(f"Sales tax amount: ${tax:.2f}");
    print(f"Grand total: ${total:.2f}");
