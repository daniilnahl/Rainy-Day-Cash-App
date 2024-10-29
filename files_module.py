"""
CSV Handling Module
This module manages recording and reading data from CSV files.

Functions:
    file_menu(transactions: list) -> None. Displays the file menu and processes user commands.
    import_or_delete_file(transactions: list, command: str) -> None. Imports or deletes a specified file.
    delete_file_action(file_name: str, files_list: list) -> None:. Deletes a specified file and updates the file list.
    import_file_action(transactions: list, file_name: str) -> None. Imports transactions from a specified file.
    files_list_update(files_list: list) -> Non. Updates the list of files from the CSV storage.
    files_list_write(files_list: list) -> None. Writes the updated file list back to the CSV storage.
    create_file(transactions: list) -> None. Prompts user to create a new CSV file for transactions.
    record_to_file_prompt(transactions: list, file_name: str) -> None. Prompts user to select the order of transactions for recording.
    record_to_file_action(transactions: list, file_name: str) -> None. Writes transactions to the specified CSV file.
    record_from_file_action(transactions: list, file_name: str) -> None. Reads transactions from the specified CSV file and updates the list.
"""
import csv
import os

def file_menu(transactions: list):
    """
    Displays the file menu and processes user commands.

    Args:
        transactions (list): A list of transactions to manage.
    """
    
    print("""FILE MENU
create - create - creates a file and be prompted to record transactions.
import - import transactions from a file (File to be imported must have been created using this application). 
delete - delete a file.
show - show all stored files.
quit - go back to main menu.  
""")
    main_menu_loop = True
    while main_menu_loop: #loop to get user input 
        user_input = input("Enter the file command you would like to do: ").lower()
        if user_input == 'create':
            create_file(transactions)  
            
        elif user_input == 'show':
            #shows all available files
            files_list = []
            files_list_update(files_list)
            print('Available files:')
            print(f'\n'.join(f'{index + 1}. {file_name}' for index, file_name in enumerate(files_list)))

        elif user_input == 'import':
            import_or_delete_file(transactions, 'import')
               
        elif user_input == 'delete':
            import_or_delete_file(transactions, 'delete')
            
        elif user_input == 'quit':
            print()
            break
        
        else:
            print('You have entered an invalid command. Please try again.')

def import_or_delete_file(transactions: list, command: str):
    """
    Imports or deletes a specified file based on user input.

    Args:
        transactions (list): A list of transactions.
        command (str): The command indicating whether to 'import' or 'delete' a file.
    """
    #intializes files list to check if such a file exists
    files_list = []
    files_list_update(files_list)
    
    #Checks if the files_list contains any file names
    if not files_list:
        print(f'No files found in the system to {command}.\n')
    else:
        print('Available files:')
        #prints all files stored in files_list
        print(f'\n'.join(f'{index + 1}. {file_name}' for index, file_name in enumerate(files_list)))
        #loop for choosing a file to import from or delete 
        while True:
            file_name = input("Enter the file's name to import transactions from: ")
            if file_name in files_list:#checks for the file to exist
                #for delete command
                if command == 'delete':
                    delete_file_action(file_name, files_list)
                    break
                #for import command
                elif command == 'import':
                    import_file_action(transactions, file_name)
                    break
            else:
                print(f'No file found with name of {file_name}') 

def delete_file_action(file_name, files_list: list):
    """
    Deletes a specified file and updates the file list.

    Args:
        file_name (str): The name of the file to delete.
        files_list (list): The current list of files to be updated.
    """
    #helper function to delete a file
    print(f'Successfully deleted {file_name}.\n')
    os.remove(file_name)
    files_list.remove(file_name)#removes the file from the list variable
    files_list_write(files_list)#update files_list file

def import_file_action(transactions: list, file_name: str):
    """
    Imports transactions from a specified file into the transactions list.

    Args:
        transactions (list): The list of transactions to append imported data to.
        file_name (str): The name of the file to import transactions from.
    """
    #helper function to import a file
    print(f'Importing transactions from {file_name}...')
    record_from_file_action(transactions, file_name)
                                                        
def files_list_update(files_list: list): #updates the list of files 
    """
    Updates the list of files from the CSV storage.

    Args:
        files_list (list): The list to be populated with file names.
    """
    try:
        with open('list_of_files.csv', 'r', encoding='utf-8') as list_of_files:
            reader = csv.reader(list_of_files)
            for file_name in reader:
                files_list.extend(file_name)#writes file names into the list
    except FileNotFoundError:
        print('File to store file names in is not found.')
            
def files_list_write(files_list: list):
    """
    Writes the updated file list back to the CSV storage.

    Args:
        files_list (list): The list of file names to be written to the storage.
    """
    try:
        with open('list_of_files.csv', 'w', newline= "", encoding='utf-8') as list_of_files:
            writer = csv.writer(list_of_files)
            writer.writerow(files_list)
    except FileNotFoundError:
        print('File for files'' name storage is not found.')        
          
def create_file(transactions: list):
    """
    Prompts user to create a new CSV file for transactions.

    Args:
        transactions (list): The list of transactions to be recorded in the new file.
    """
    #updates the list of files that already exist
    files_list = []
    files_list_update(files_list)
    
    file_name = input('How would you like to name your file? Enter here: ') + '.csv'#for file type
    
    while True:
        if file_name in files_list:#checks if the file already exists
            print("File with such a name already exists.")
            break
        
        try:#creates the file
            with open(file_name, 'w+', encoding='utf-8') as current_file:
                print(f"Succesfully create a file by the name of {file_name}\n")
        except IOError:#catches an error in creating a file
            print('An error occurred: {IOError}')
        
        #updates the files list
        files_list.append(file_name)
        #updates the list_of_files.csv
        files_list_write(files_list)
        
        record_to_file_prompt(transactions, file_name)
        break
        
def record_to_file_prompt(transactions: list, file_name: str):    
    """
    Prompts user to select the order for recording transactions into a file.

    Args:
        transactions (list): The list of transactions to be recorded.
        file_name (str): The name of the file to store recorded transactions.
    """ 
    
    print("""In what order would you like to record transactions?
1 - order in which transactions were made.
2 - ascending by amount.
3 - descending by amount.""")
    
    #temporary list to store transactions for recording.
    temp_transactions = []
    user_input_loop = True
    #loop for user input
    while user_input_loop:
        try:
            user_input = int(input('Enter here: '))
            if user_input == 1:
                print('Recording in original order...')
                temp_transactions = transactions
                break
            elif user_input == 2:
                print('Recording in ascending order...')
                temp_transactions = sorted(transactions, key=lambda t: t[0], reverse=False)
                break
            elif user_input == 3:
                print('Recording in descending order...')
                temp_transactions = sorted(transactions,  key=lambda t: t[0], reverse=True)
                break
            else:
                print('Invalid command. Enter a number as specified above.') 
        except ValueError:
            print('Invalid input type. Please enter an integer number.')    
    
    #records into file based on order user chose
    record_to_file_action(temp_transactions, file_name)
   
def record_to_file_action(transactions, file_name):
    """
    Writes transactions to the specified CSV file.

    Args:
        transactions (list): The list of transactions to write to the file.
        file_name (str): The name of the file to store transactions.
    """
    
    with open(file_name, 'w', newline = "", encoding='utf-8') as current_file: #reworked this for csv
        writer = csv.writer(current_file)#created an object to write
        for transaction in transactions:
            writer.writerow(transaction)#wrote data into file 
    print('Transactions succesfully stored.\n')
    
def record_from_file_action(transactions: list, file_name: str):
    """
    Reads transactions from the specified CSV file and updates the transacations list.

    Args:
        transactions (list): The list of transactions to collect imported data.
        file_name (str): The name of the file to read transactions from.
    """
    
    with open(file_name, 'r', newline = "", encoding='utf-8') as current_file: 
        reader = csv.reader(current_file)#created an object to write
        for transaction in reader:
            try:
                #break the transaction in two parts
               amount = float(transaction[0])
               date = transaction[1] 
               transactions.append([amount, date])#assembles the transactions from the parts into one and stores it
            except (ValueError, IndexError):
                #skips if not enough elements to create a transaction
                continue
    print('Transactions successfully imported.\n')