
"""Module for handling functions for recording and reading data from and to CSV files."""
import csv
#add function to delete files
#add function to modify files
#add function to write in already exisitng files

def file_menu(transactions: list):
    print("""FILE MENU
create - creates a file and get prompted to record transactions.   
show - show all stored files.
quit - go back to main menu.  
""")
    
    while True: #loop to get user input 
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
        elif user_input == 'quit':
            break
        else:
            print('You have entered an invalid command. Please try again.')
            
def files_list_update(files_list: list): #updates the list of files 
    """Updates global files_list using data stored in list_of_file.csv when the app starts up"""
    try:
        with open('list_of_files.csv', 'r', encoding='utf-8') as list_of_files:
            reader = csv.reader(list_of_files)
            for file_name in reader:
                files_list.extend(file_name)
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
    #loop for user input
    while True:
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
        #auto closes
    print('Transactions succesfully stored.\n')

    
