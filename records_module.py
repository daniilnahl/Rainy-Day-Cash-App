"""Module with functions created to record user's transactions"""

def another_transaction() -> bool:
    """
    Ask user if they want to record another transaction.
    Return:
        (bool): True or False for 'yes' and 'no' accordingly.
    """
    print('Would you like to record another transaction?')
    while True:
        another_transaction_input = input('Enter here(yes/no): ').lower()  

        if another_transaction_input == 'yes':
            return True
        elif another_transaction_input == 'no':
            return False
        else: 
            print('You have entered an invalid command. Please try again.')
            continue
                

def type_of_transaction() -> int:
    """
    Gets user input on what kind of transaction they want and returns a positive or negative number.
    Return:
        value (int): -1 for withdrawl, 1 for deposit.
    """

    print('Is the transaction a deposit or withdrawal?')
    transaction_type = input('+ for deposit, - for withdrawal. Enter here: ')

    while True:      
            if transaction_type == '+':
                return 1  # Deposit, so no negative sign    
            elif transaction_type == '-':
                return -1   
            else:
                print('You have entered an invalid type. Please try again.')
                transaction_type = input('+ for deposit, - for withdrawal. Enter here: ')
                continue
    
        
def recording_transaction(transaction_type: int, transactions_list: list):
    """
    Processes a transaction by determining its type (deposit or withdrawal) 
    and prompts the user for a valid transaction amount. The function 
    appends the transaction amount to the transactions list depending on 
    its type (positive for deposits, negative for withdrawals).

    Args:
        transaction_type (int): -1 for withdrawl, 1 for deposit.
        transactions_list (list): A list which stores transactions.
    """
    while True:
        try:# Keep prompting the user until a valid number is entered
            amount = float(input('Enter the amount: '))
            print(f'You have recorded a transaction of ${amount}.\n')
            transactions_list.append(transaction_type * amount)#records positive amount if addition of money
            break
        except ValueError:
            # If the user enters something that's not a number, this message will show
            print('Invalid input. Please enter a valid number.')
    

