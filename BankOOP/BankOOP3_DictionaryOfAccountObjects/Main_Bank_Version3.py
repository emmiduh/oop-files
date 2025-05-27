# Test program using accounts
# Version 3, using explicit variables for each Account object

# Bring in all the code from the Account class file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Account import *

accountDict = {}
nextAccountNumber = 0

# Create two accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountDict[joesAccountNumber] = oAccount
print('Account number for Joe is:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountDict[marysAccountNumber] = oAccount
print('Account number for Mary is:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Call some methods on the different accounts
print('Calling methods of the two accounts')
accountDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Show the accounts
accountDict[joesAccountNumber].show()
accountDict[marysAccountNumber].show()

print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the start balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Show the newly created user account
accountDict[newAccountNumber].show()

# Let's deposit 100 into the new account
accountDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountDict[newAccountNumber].getBalance(userPassword)
print()
print(f"After depositing 100, {userName}'s balance is: {userBalance}")

# SHow the new account
accountDict[newAccountNumber].show()