# Bank that manages a dictionary of Account objects

from Account import *

class Bank():
    def __init__(self, workingHours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.workingHours = workingHours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer') 
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account ' + str(accountNumber))
        return accountNumber
    
    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount
     
    def askForValidPassword(self, account):
        userPassword = input('Enter your password: ')
        if userPassword != account.password:
            raise AbortTransaction('Incorrect password for this account')
        return userPassword
    
    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)
    
    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[userAccountNumber]
        userAccountPassword = input("Enter your password: ")
        if userAccountPassword != oAccount.password:
            print("Incorrect password.")
            return
        theBalance = oAccount.getBalance()
        if theBalance is not None:
            print('Your balance is:', theBalance)    

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
        userPassword = input("Enter your password: ")
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountnumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[userAccountnumber]
        userPassword = self.askForValidPassword(oAccount)
        theBalance = oAccount.getBalance()
        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you')
            del self.accountsDict[userAccountnumber]
            print('Your account is now closed')

    def getInfo(self):
        print('workingHours:', self.workingHours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print(f'We currently have {len(self.accountsDict)} account(s) open.')

    def show(self):
        print('*** Show ***')
        print('(This would typically require and admin password)')
        if len(self.accountsDict) == 0:
            raise AbortTransaction('There are currently zero accounts to show. Press o to open a new account')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print(f'Account: {userAccountNumber}')
            oAccount.show()
            print()