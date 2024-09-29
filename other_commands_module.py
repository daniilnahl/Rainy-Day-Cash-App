"""
Other Commands Module
This module provides functionality for displaying, modifiying and deleting transactions.

Functions:
    show_transactions(type_of_command: str, transactions: list) -> None.  Displays the current list of transactions based on a specified command.
    mod_or_del_transaction(command_type: str, transactions: list) -> None. Modifies or deletes a transaction based on user input.
    modifying_transaction_choice(transactions: list, transaction_index: int) -> None.  Modifies the time or amount of a specified transaction.
    modifying_transaction_amount() ->Returns a new amount for the modified transaction based on user input.
    modifying_transaction_date() -> Returns a new date for the modified transaction based on user input.
    loop_for_date(time_type: str, month=0) -> Returns components of a formatted date based on user input for year, month, or day.
"""

def show_transactions(type_of_command: str,transactions: list):
    """
    Display transactions based on the command type.

    Args:
        type_of_command (str): Specifies how to display transactions.
        transactions (list): A list of transactions to be displayed.

    Returns:
        None
    """
    transactions_showcase = f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))
    
    if type_of_command == 'delete':
        print(f'CHOOSE A TRANSACTION TO DELETE\n{transactions_showcase}')
    elif type_of_command == 'transactions':
        print(f'VIEWING ALL TRANSACTIONS\n{transactions_showcase}')
    elif type_of_command == 'modify':
         print(f'CHOOSE A TRANSACTION TO MODIFY\n{transactions_showcase}')

def mod_or_del_transaction(command_type: str, transactions: list):
    """
    Modifies or deletes a transaction based on user input.

    Args:
        command_type (str): Specifies whether to 'modify' or 'delete' a transaction.
        transactions (list): A list of transactions to modify or delete.

    Returns:
        None
    """
    if command_type == 'modify':
        show_transactions('modify', transactions)
    elif command_type == 'delete':
        show_transactions('delete', transactions)

    print(f'Enter the number before the transaction that you would like to {command_type}.')
    while True:
        try: 
            #Prompts user to enter a valid label 
            modify_transaction = int(input('Enter here: ')) 
            #calculates transaction's index
            transaction_index = modify_transaction - 1 
            #checks if the transaction_index  is within bounds 
            if transaction_index not in range(len(transactions)): 
                print(f"The transaction you want to {command_type} is out of bounds and doesn't exist.")
                
            else:
                if command_type == 'modify':   
                    modifying_transaction_choice(transactions, transaction_index)
                elif command_type == 'delete':
                    print(f"Succesfully deleted {transactions[transaction_index]}\n")
                    del transactions[transaction_index]#deletes the transaction element  
                break                   
        except ValueError:# Handle invalid input that isn't an integer
            print('Invalid input type. Please enter an integer number corresponding to a transaction.')

def modifying_transaction_choice(transactions: list, transaction_index: int):
    """
    Prompt user to modify the amount or date of a specific transaction.

    Args:
        transactions (list): A list of transactions.
        transaction_index (int): The index of the transaction to modify.

    Returns:
        None
    """
    print(f'{transactions[transaction_index]} Would you like to modify the amount or date?')
    while True:
        try:
            modified_part = int(input('Enter 0 for amount, and 1 for date: '))
            #modifies the amount
            if modified_part == 0:
                transactions[transaction_index][0] = modifying_transaction_amount() 
                break
            #modifies the date
            elif modified_part == 1: 
                #stores the new date
                transactions[transaction_index][1] = modifying_transaction_date() 
                break
            else:#if user doesnt enter a num for amount or date
                print('No modifiable data at this number.')
                continue
        except ValueError:
            print('Invalid input type. Please enter an integer.') 
    
def modifying_transaction_amount():
    """
    Gets a new amount for the modified transaction.

    Returns:
        float: The new amount for the transaction.
    """

    while True:
        try: 
            modified_amount = float(input('Enter the replacament amount: '))
            print(f'Successfully assigned new value. Now the amount is {modified_amount}.\n')
            return modified_amount#assigns the new amount 
            
        except ValueError:#handles input which cant be converted to a float
            print('You have entered an invalid input type. Please enter an int or float number.')
    
def modifying_transaction_date():
    """
    Get a new date for the modified transaction.

    Returns:
        str: The new date formatted as 'YYYY-MM-DD'.
    """

    modified_date = ''
    modified_month = ''

    modified_date += loop_for_date('year') + '-'
    #doesnt directly assign to new date because we need to use the month to set the limit for day
    modified_month = loop_for_date('month')
    modified_date += modified_month + '-'
    modified_date += loop_for_date('day', int(modified_month))
    
    print(f'Successfully assigned new date. Now the date is {modified_date}.\n')
    return modified_date

def loop_for_date(time_type: str, month=0) -> str:
    """
    Gets a part for the formatted date based on the specified time type(year, month, or day).

    Args:
        time_type (str): Specifies whether to get a year, month, or day.
        month (int, optional): The month to determine the valid range for days. Defaults to 0.

    Returns:
        str: The validated input.
    """
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
            print(f'Invalid input type. Please enter an integer for the {time_type}. ERROR LFD')           
