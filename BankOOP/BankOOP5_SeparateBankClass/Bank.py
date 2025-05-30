# Bank that manages a dictionary of Account objects
# 
# # Bring in all the code from the Account class file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Account import *

class  Bank():
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber
    
    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new account? ')
        userStartingAmount = input('What is the starting balance for the account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to sue for the account? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountnumber = input('What is your account number? ')
        userAccountnumber = int(userAccountnumber)
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountnumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you')
            del self.accountsDict[userAccountnumber]
            print('Your account is now closed')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount  = int(depositAmount)
        useraccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]
        theBalance = oAccount.deposit(depositAmount, useraccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('     Account Number:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter the password you want to use for the account: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)