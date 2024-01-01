"""
Name: Brandon Perez
Class: CSCI 1411-006
Due Date: 11/30/23
Description: Lab 13
Status: works as expected
"""

class BankAccount:
    def __init__(self):
        '''Defines the BankAccount class'''
        self.balance = 0

    def deposit(self, amount):
        '''deposits money into the balance'''
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        '''withdraws amount from balance'''
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def getBalance(self):
        '''returns the current balance'''
        return self.balance

    
