# BankAccount.py
# Author: Brandon A. Perez
# Date: 12/1/23

#import Transaction class
from Transaction import *

def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Add a new transaction')
        print ('B - Calculate current balance')
        print ('C - Display list of transactions')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C,or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            add_transaction (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            calculate_balance (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            display_list (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')


def display_list(transactions):
    """ Displays list of transactions """
    print(f'\n{" ID":3}{"| Date":12}{"| Amount":9}{"| Type of Transaction":20}')
    print('============================================')
    for i in range(len(transactions)):
        print(f'{i+1:3}{"| " + transactions[i].get_date():12}{f"| ${transactions[i].get_amount():.2f}":9}{"| " + transactions[i].get_transaction_type():20}')
    print()
   
           
def add_transaction(transactions):
    """Adds a new transaction to list of Transactions"""

    date = input('Date: ')
    type_of_trans = input('Type: ')
    amount = int(input('Amount: $'))
    transactions.append(Transaction(date, type_of_trans, amount))
        
    # Ask user for date, type, and amount of transaction, create a transaction
    # object and append it to the list of transactions.
    # Display an error message if the transaction type is not valid or amount
    # is negative. Valid transaction types are deposit, withdraw, bank charge
    # and interest

def calculate_balance (transactions):

    """Calculates the current balance"""
    balance = 0
    for trans in transactions:
        amount = trans.get_amount()
        t = trans.get_transaction_type()

        if t=='bank charge' or t=='withdraw':
            balance -= amount
        else:
            balance += amount
    print(f'\nYour current balance is ${balance:.2f}\n')

    # Start with initializing balance to zero
    # For each transaction in the list of transactions you will
    # add the amount to balance if the transaction type is deposit or interest
    # subtract the amount if transaction type is withdraw or bank charge
    # Print the balance on the screen
            
        


            
