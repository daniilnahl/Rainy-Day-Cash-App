"""Module for handling functions for recording and reading data from and to CSV files."""

#function to present user the available commands in the file menu 
def file_menu():
    print("""
    FILE MENU
    open - open a file. If a file with a name provided does not exist it will create a new one.
    record - records transactions into the file.   
    quit - go back to main menu.  
    """)
    
    while True: #loop to get user input 
        user_input = input("Enter the command you would like to do: ").lower()
        if user_input == 'open':
            create_file()

        elif user_input == 'record':
            record_to_file()
        
        elif user_input == 'quit':
            break
        
        else:
            print('You have entered an invalid command. Please try again.')
            
        

#function to open a file

#function to create a file
def create_file():
    file = open('transactions.txt', 'w+', encoding='utf-8')
    
    file.close
    

#function to write in a file 
def record_to_file(transaction):
    
    transactions_text = f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))
    file.write(transactions_text)