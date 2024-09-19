"""
Rainy Day Cash App Module

This module allows users to track their saved cash for a "rainy day." 
It provides features for recording deposits and withdrawals, viewing 
all transactions, and calculating the total balance.

Functions:
    welcome_message(): 
        Displays a welcome message and an overview of the app's purpose.

    command_list(): 
        Prints a list of available commands in the app.

    total_amount(transactions: list) -> float: 
        Calculates and returns the total balance of transactions.
"""

def welcome_message():
    print("""
    Welcome to Raindy Day Cash App!
Here you can track how much cash you have saved for your "rainy" day.
The current features are adding and removing deposits, and viewing the 
total amount saved.
          
Discalimer:
This app is only a tracker and is here to help you keep tabs on how
much money you have set aside. The physical process of putting the 
money into a stash is a responsibility of the user.               
""")

def command_list():
    print("""COMMAND LIST
record - record a transaction to the tracker.
transactions - view all transactions.      
total - view the total amount.
help - view the command list.
quit - quits the program.
""")

def total_amount(transactions: list) -> float:
    """
    Calculates the total balance of user's transactions.

    Args:
    transactions(list of float values): A list of the user's transaction amounts. Positive values indicate deposits, while negative values represent withdrawals.

    Return:
    float: total balance after summing up all transactions. 
    """

    return round(sum(transactions[0]), 2)
