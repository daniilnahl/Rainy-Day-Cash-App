"""
Other Commands Module
This module provides functionality for displaying, modifiying and deleting transactions.

Functions:
    show_transactions(type_of_command: str, transactions: list) -> None.  Displays the current list of transactions based on a specified command.
    delete_transaction(transactions: list) -> None  Prompts the user to delete a transaction.
    modify_transaction(transactions: list) -> None Prompts the user to modify a transaction. 
"""

def show_transactions(type_of_command: str,transactions: list):
    """
    Display transactions based on the command type.

    Args:
        type_of_command (str): A command that determines how transactions are displayed. 
            - If 'delete', it displays all transactions with header "CHOOSE A TRANSACTION TO DELETE".
            - If 'transactions', it displays all transactions with header "VIEWING ALL TRANSACTIONS".
        transactions (list): A list of transactions to be displayed.

    Returns:
        None: Prints the transactions in the appropriate format based on the command.
    """
    transactions_showcase = f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))
    
    if type_of_command == 'delete':
        print(f'CHOOSE A TRANSACTION TO DELETE\n{transactions_showcase}')
    elif type_of_command == 'transactions':
        print(f'VIEWING ALL TRANSACTIONS\n{transactions_showcase}')
    elif type_of_command == 'modify':
         print(f'CHOOSE A TRANSACTION TO MODIFY\n{transactions_showcase}')


def delete_transaction(transactions):
    """
    Prompt the user to delete a transaction from the list.

    Args:
        transactions (list): A list of transactions to choose from for deletion.

    Returns:
        None: function deletes the specified transaction and stops once a valid deletion is made.
    """

    show_transactions('delete',transactions)
    print('Enter the number before the transaction that you would like to delete.')
    while True:
            try: 
                #Prompts user to enter a valid label 
                delete_transaction = int(input('Enter numbered label: ')) 
                #calculates transaction index
                transaction_index = delete_transaction - 1 

                #checks if the transaction_index  is within bounds 
                if transaction_index not in range(len(transactions)): 
                    print("The transaction you want to delete is out of bounds and doesn't exist.")
                
                else:
                    print(f"Succesfully deleted transaction {delete_transaction}. {transactions[transaction_index]}\n")
                    del transactions[transaction_index]#deletes the transaction element
                    break
            
            except ValueError:# Handle invalid input that isn't an integer
                 print('Invalid input. Please enter an integer number corresponding to a transaction.')

def modify_transaction(transactions):
    show_transactions('modify', transactions)
    print('Enter the number before the transaction that you would like to modify.')
    while True:
        try: 
            #Prompts user to enter a valid label 
            modify_transaction = int(input('Enter here: ')) 
            #calculates transaction index
            transaction_index = modify_transaction - 1 

            #checks if the transaction_index  is within bounds 
            if transaction_index not in range(len(transactions)): 
                print("The transaction you want to modify is out of bounds and doesn't exist.")
                
            else:
                print(f'{transactions[transaction_index]} Would you like to modify the amount or date?')
                while True:
                    try:
                        modified_part = int(input('Enter 0 for amount, and 1 for date: '))
                        #modifies the amount
                        if modified_part == 0:
                            while True:
                                    try: 
                                        modified_amount = float(input('Enter the replacament amount: '))
                                        print(f'Successfully assigned new value. Now the amount is {modified_amount}.')
                                        transactions[transaction_index][0] = modified_amount#assigns the new amount 
                                        break
                                    except ValueError:#handles input which cant be converted to a float
                                        print('You have entered an invalid amount. Please enter a number.')
                            break#stops the loop for choosing the modifying part
                        #modifies the date
                        elif modified_part == 1: 
                            #stores the new date
                            new_date = modifying_transaction_date()
                            transactions[transaction_index][1] = new_date#assigns the new date 
                            break
                        else:#if user doesnt enter a num for amount or date
                            print('No modifiable data at this number.')
                            continue
                    except ValueError:
                        print('Invalid input. You can only enter an integer number. ERROR MOD TRNS')
                break                   
        except ValueError:# Handle invalid input that isn't an integer
            print('Invalid input. Please enter an integer number corresponding to a transaction.')
        
            
def modifying_transaction_date():
    modified_date = ''
    modified_month = ''

    modified_date += loop_for_date('year') + '-'
    #doesnt directly assign to new date because we need to use the month to set the limit for day
    modified_month = loop_for_date('month') + '-'
    modified_date += modified_month
    modified_date += loop_for_date('day', int(modified_month))
    
    return modified_date

def loop_for_date(time_type: str, month=0) -> str:
    """"""
    #variables for bounds of user input
    bottom_limit = 0
    top_limit = 0

    #assigns the limits based on type of time 
    if time_type == 'year':
        bottom_limit = 2000
        top_limit = 3000          
    elif time_type == 'month':
        bottom_limit = 1
        top_limit = 12        
    elif time_type == 'day':
        bottom_limit = 1
        #dictionary for days in each month by their calendaric number
        days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        top_limit = days_in_months[month] #assigns the limit of days by the month user entered
        
    while True:#loops until the user enters a valid amount for specified type of time
        try:
            modified_num = int(input(f'Enter the {time_type}: '))
            #checks the limits
            if modified_num >= bottom_limit and modified_num <= top_limit: 
                return str(modified_num)#returns the string version of modded num
            else:
                print(f'The value of {time_type} must be between {bottom_limit} and {top_limit}. Try again.')
        except ValueError:
            print(f'Invalid input. Please enter an integer for the {time_type}. ERROR LFD')           
