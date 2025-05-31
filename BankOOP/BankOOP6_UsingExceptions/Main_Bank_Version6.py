# Main program for controlling a Bank made up of Accounts

from Bank import *

# Create an instance of the Bank
oBank = Bank('9 to 5', '123 Main Street, Anytown, USA', '(650) 555-1212')

# Main code
while True:
    print()
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To get an account balance, press b')
    print('To make a deposit, press d')
    print('To make a withdrawal, press w')
    print('To close an account, press c')
    print('To show all accounts, press s')
    print('To quit, press q')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 's':
            oBank.show()    
        elif action == 'o':
            oBank.openAccount()
        elif action == 'q':
            break
        elif action == 'w':
            oBank.withdraw()
    except AbortTransaction as error:
        print(error)

print('Done')