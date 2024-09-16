"""Module with functions created to record user's transactions"""

def type_of_transaction(transaction_type: str, transactions_list: list):
    """
    Processes a transaction by determining its type (deposit or withdrawal) 
    and prompts the user for a valid transaction amount. The function 
    appends the transaction amount to the transactions list depending on 
    its type (positive for deposits, negative for withdrawals).

    Args:
        transaction_type (str): The type of transaction ('+' for deposit, '-' for withdrawal).
        transactions_list (list): A list which stores transactions.
    """
    sign = 0
    if transaction_type == '+':
            sign = 1  # Deposit, so no negative sign
    elif transaction_type == '-':
            sign = -1

    while True:
        try:# Keep prompting the user until a valid number is entered
            amount = float(input('Enter the amount: '))
            print(f'You have recorded a transaction of ${amount}.\n')
            transactions_list.append(sign * amount)#records positive amount if addition of money
            break
        except ValueError:
            # If the user enters something that's not a number, this message will show
            print('Invalid input. Please enter a valid number.\n')
    