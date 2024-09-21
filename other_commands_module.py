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
    return 1
        
            
   