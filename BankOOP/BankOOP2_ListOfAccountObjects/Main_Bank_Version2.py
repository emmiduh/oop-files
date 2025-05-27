# Test program using accounts
# Version 2, using a list of acounts

# Bring in all the code from the Account class file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Account import *

# Start off with an empty list of accounts
accountsList = []

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Mary's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

# Show the accounts
accountsList[0].show()
accountsList[1].show()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want for this account? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

# Show the newly created user account
print('Created new account, account number is 2')
accountsList[2].show()

# Let' deposit 100 into the new account
accountsList[2].deposit(100, userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print(f"After depositing 100, {userName} balance is: {userBalance}")

# Show the new account
accountsList[2].show()

