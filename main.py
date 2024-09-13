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
    print("""
    COMMAND LIST
    add - add a money deposit to the tracker.
    remove - remove an amount from the total. 
    total - view the total amount.
    transactions - view all transactions.
    """)

def total_amount(transactions: list) -> float:
    return round(sum(transaction for transaction in transactions))
    

    
def main():
    #welcome message
    welcome_message()
    command_list()
    
    #variables
    transactions = []  

    while True:
        #updates the total amount of money with each cycle 
        total = total_amount(transactions)

        command = input("Enter the command you would like to do: ").lower()

        #adds money
        if command == 'add':    
            amount = float(input('Enter the amount you stashed away: '))
            transactions.append(amount)
        #removes money
        elif command == 'remove':
            amount = float(input('Enter the amount you removed from the stash: '))
            transactions.append(-amount)

            print(f'You removed ${amount} from {total}. You are left with ${round(total-amount)}')
        #shows total money
        elif command == 'total':
            print(f'Your total is ${total}')
        elif command == 'transactions':
            #add code for this
        else:
            print('You have entered an invalid command. Please try again.')
        
        



if __name__ == "__main__":
    main()