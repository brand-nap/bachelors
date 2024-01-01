"""
Name: Brandon Perez
Class: CSCI 1411-006
Due Date: 11/30/23
Description: Lab 13
Status: works as expected
"""
from BankAccount import *

def main():
    acct = BankAccount()
    count = int(input('How many transactions would you like: '))
    transactions = [0,0]
    for i in range(count):
        wd = input('Which kind of transaction would you like: ') == 'withdrawal'
        amt = float(input(f'Amount you\'d like to {"withdraw" if wd else "deposit"}: '))
        if wd:
            if acct.withdraw(amt):
                transactions[1] = transactions[1]+1
                print(f"Transacation was successful. Your account balance is ${acct.getBalance():.2f}")
            else:
                print(f"Withdrawal amount ${amt:.2f} is greater than balance ${acct.getBalance():.2f}.")
                print("Transaction rejected")
        
        else:
            if acct.deposit(amt):
                transactions[0] = transactions[0]+1
                print(f"Transacation was successful. Your account balance is ${acct.getBalance():.2f}")
            else:
                print(f"Deposit amount ${amt:.2f} is less than 0. Transaction rejected")
    print(f'After {transactions[0] + transactions[1]} successful transactions your account balance is ${acct.getBalance():.2f}')

    
