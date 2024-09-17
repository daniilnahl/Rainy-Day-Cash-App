import records_module as rm

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

    return round(sum(transaction for transaction in transactions), 2)
     
def main():
    #welcome message with initial view of the commands
    welcome_message()
    command_list()
    
    #variables
    transactions = []  

    while True:
        #updates the total amount of money with each cycle 
        total = total_amount(transactions)

        command = input("Enter the command you would like to do: ").lower()
        print()

        #records a transaction
        if command == 'record':  
            print('You have chosen to record a transaction.')
            #boolean used to check the status of the transaction. Used later to check if user wants to record another transaction. 
            transaction_status = True
            while True:
                while transaction_status: #loop to get the user to enter a transaction
                    #gets user input on what kind of transaction it is 
                    print('Is the transaction a deposit or withdrawal?')
                    type_of_transaction = input('+ for deposit, - for withdrawal. Enter here: ')
                    #records the transaction and its type into the transactions list
                    rm.recording_transaction(rm.type_of_transaction(type_of_transaction), transactions)
                    transaction_status = False #sets the loop to false
                   
                #checks if user wants to add another transaction 
                print('Would you like to record another transaction?')
                another_transaction = input('Enter here(yes/no): ').lower()  

                if another_transaction == 'yes':
                    transaction_status = True

                elif another_transaction == 'no':
                    print()
                    break

                else: 
                    print('You have entered an invalid command. Please try again.\n')
                    continue
                

        #shows total amount stored
        elif command == 'total':
            print(f'Your total is ${total}\n')

        #shows all the recorded transactions
        elif command == 'transactions':
            print('\n'.join(str(transaction) + '$' for transaction in transactions))

        elif command == 'quit':
            break   

        elif command == 'help':
            command_list()

        else:
            print('You have entered an invalid command. Please try again.\n')
        

        #FOR FUTURE
        #1. Modularize code.
        #1.5 Modify code in such way that the input must be specific type and that it will loop until the input is of that type
        #2. Add a feature that will automatically record when a transaction was made.
        #3. Adds features to show transactions in orderL ascedning amount, descending amount, by date. 
if __name__ == "__main__":
    main()