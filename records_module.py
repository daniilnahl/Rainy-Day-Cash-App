"""
Transaction Recording Module

This module provides functions to interactively record and manage 
user transactions, such as deposits and withdrawals. It includes 
functions for user input validation, handling transaction types, 
and updating a list of transactions.

Functions:
    get_another_transaction() -> bool:
        Asks the user if they want to record another transaction.

    get_typeof_transaction() -> int:
        Gets the user's input for the type of transaction 
        (deposit or withdrawal) and returns 1 for deposit or -1 for withdrawal.

    recording_transaction(transaction_type: int, transactions_list: list):
        Prompts the user for a valid transaction amount and appends 
        the value to the transactions list.

    record_loop(transactions: list):
        Main loop that handles recording multiple transactions and 
        checks if the user wants to continue recording transactions.
"""
import time

def get_another_transaction() -> bool:
    """
    Ask user if they want to record another transaction.
    Return:
        (bool): True or False for 'yes' and 'no' accordingly.
    """
    print('Would you like to record another transaction?(yes/no)')
    while True:
        another_transaction_input = input('Enter here: ').lower()  

        if another_transaction_input == 'yes':
            return True
        elif another_transaction_input == 'no':
            return False
        else: 
            print('Invalid input. Please enter yes or no')
            continue
                

def get_transaction_type() -> int:
    """
    Gets user input on what kind of transaction they want and returns a positive or negative number.
    Return:
        value (int): -1 for withdrawl, 1 for deposit.
    """
    DEPOSIT = 1
    WITHDRAWAL = -1

    print('Is the transaction a deposit or withdrawal? + for deposit, - for withdrawal.')
    while True: 
            transaction_type = input('Enter here: ')
     
            if transaction_type == '+':
                return DEPOSIT  
            elif transaction_type == '-':
                return WITHDRAWAL
            else:
                print('Invalid input. Please enter + or -')
                continue
    
        
def recording_transaction(transaction_type: int, transactions_list: list):
    """
    Records a transaction based on its type (deposit or withdrawal) and 
    prompts the user for a valid amount. The amount is added to the 
    transactions list as positive for deposits and negative for withdrawals.
    Additionally, records the date of the transaction.

    Args:
        transaction_type (int): -1 for withdrawl, 1 for deposit.
        transactions_list (list): A list which stores transactions.
        Each transaction is a list which holds the amount and date.
    """
    #temporary list to hold transaction information
    transaction = []
    while True:
        try:# Keep prompting the user until a valid number is entered
            time_during_transaction = time.localtime() #
            amount = float(input('Enter the amount: '))
            print(f'You have recorded a transaction of ${amount}.\n')
            transaction.append(transaction_type * amount)#records positive amount if addition of money
            transaction.append(time.strftime("%Y-%m-%d", time.localtime()))#records the date the transaction was made
            transactions_list.append(transaction)#records the transaction into list of transactions
            break
        except ValueError:
            # If the user enters something that's not a number, this message will show
            print('Invalid input. Please enter a valid number.')
    

def record_loop(transactions):
    """
    Main loop of recording user's transactions. Records user's transactions and prompts him to record more if wanted.

    Args:
        transactions (list): list consiting of float values which represent user's transactions.
    """
    #boolean used to check the status of the transaction. Used later to check if user wants to record another transaction. 
    transaction_status = True
    while True:#main loop
        while transaction_status: 
            transaction_type = get_transaction_type() #determines if deposit or withdrawal
            recording_transaction(transaction_type, transactions)
            transaction_status = False #sets the loop to false

        #checks if user wants another transaction
        if get_another_transaction():
            transaction_status = True #resets loop
        else:
            break
    print()#space for readability after function ended
    
    