# Bank that manages a dictionary of Account objects

from Account import *

class bank():
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer') 
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account' + str(accountNumber))
        return accountNumber
    
    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount
    
    def askForValidPassword(self):
        userPassword = input('Enter your password')
        if userPassword != self.password:
            raise AbortTransaction('Incorrect password for this account')
    
    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print(f'We currently have {len(self.accountsDict)} account(s) open.')

    def show(self):
        print('*** Show ***')
        print('(This would typically require and admin password)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print(f'Account: {userAccountNumber}')
            oAccount.show()
            print()