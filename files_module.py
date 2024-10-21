
"""Module for handling functions for recording and reading data from and to CSV files."""
import csv
import os

def file_menu(transactions: list):
    print("""FILE MENU
create - creates a file and get prompted to record transactions.  
import - import transactions from a file (File to be imported must have been created using this application). 
delete - delete a file.
show - show all stored files.
quit - go back to main menu.  
""")
    main_menu_loop = True
    while main_menu_loop: #loop to get user input 
        user_input = input("Enter the file command you would like to do: ").lower()
        if user_input == 'create':
            current_file = create_file(transactions)  
            print(current_file)  
            
        elif user_input == 'show':
            #shows all available files
            temp_files_list = []
            files_list_update(temp_files_list)
            print('Available files:')
            print('\n'.join(temp_files_list))
            print()
        
        elif user_input == 'import':
            import_from_file()
               
        elif user_input == 'delete':
            delete_file()
            
        elif user_input == 'quit':
            print()
            break
        
        else:
            print('You have entered an invalid command. Please try again.')

def import_from_file(transactions):
    #intializes files list to check if such a file exists
    files_list = []
    files_list_update(files_list)
    
    #loop for choosing a file to import from
    while True:
        file_name = input("Enter the file's name to import transactions from: ")
        if file_name in files_list:#checks for the file to exist
            print(f'Importing files from {file_name}...')
            
            break
        else:
            print(f'No file found with name of {file_name}')  
                   
def delete_file():
    #intializes files list to check if such a file exists
    files_list = []
    files_list_update(files_list)
    
    #loop to delete file using user input
    while True: 
        file_name = input("Enter the file's name you want to delete: ")
        if file_name in files_list:#checks for the file to exist
            print(f'Succesfully deleted {file_name}\n')
            os.remove(file_name)
            files_list.remove(file_name)#removes the file from the list variable
            break
        else:
            print(f'No file found with name of {file_name}')   
    #updates the files list file after deleting a file
    files_list_write(files_list)
        
          
                        
def files_list_update(files_list: list): #updates the list of files 
    """Updates global files_list using data stored in list_of_file.csv when the app starts up"""
    try:
        with open('list_of_files.csv', 'r', encoding='utf-8') as list_of_files:
            reader = csv.reader(list_of_files)
            for file_name in reader:
                files_list.extend(file_name)#writes file names into the list
    except FileNotFoundError:
        print('File for files'' name storage is not found.')
            
def files_list_write(files_list: list):
    """Writes updated files list into the csv file"""
    try:
        with open('list_of_files.csv', 'w', newline= "", encoding='utf-8') as list_of_files:
            writer = csv.writer(list_of_files)
            writer.writerow(files_list)
    except FileNotFoundError:
        print('File for files'' name storage is not found.')        
          
def create_file(transactions: list):
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
    print("""In what order would you like to record transactions?
1 - order in which transactions were made.
2 - ascending by amount.
3 - descending by amount.""")
    
    #temp transactions for rtfa function
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
                ('Recording in descending order...')
                temp_transactions = sorted(transactions,  key=lambda t: t[0], reverse=True)
                break
            else:
                print('Invalid command. Enter a number as specified above.') 
        except ValueError:
            print('Invalid input type. Please enter an integer number.')    
    
    #records into file based on order user chose
    record_to_file_action(temp_transactions, file_name)
   
def record_to_file_action(transactions, file_name):
    with open(file_name, 'w', newline = "", encoding='utf-8') as current_file: #reworked this for csv
        writer = csv.writer(current_file)#created an object to write
        for transaction in transactions:
            writer.writerow(transaction)#wrote data into file 
    print('Transactions succesfully stored.\n')
    
def record_from_file_action(transactions: list, file_name: str):
    with open(file_name, 'r', newline = "", encoding='utf-8') as current_file: 
        reader = csv.writer(current_file)#created an object to write
        for transaction in reader:
            transactions.extend(transaction)
    print('Transactions succesfully imported.\n')