
"""Module for handling functions for recording and reading data from and to CSV files."""
import csv


files_list = [] #list for all file names [WOULD NEED TO BE UPDATED EACH TIME WHEN THE APP RESTARTS UNLESS THERE IS ANOTHER WAY TO CHECK]

def file_menu(transactions: list):
    print("""FILE MENU
create - creates a file. 
record - records transactions into a file.   
quit - go back to main menu.  
""")
    
    
    while True: #loop to get user input 
        user_input = input("Enter the file command you would like to do: ").lower()
        if user_input == 'create':
            current_file = create_file(transactions)  
            print(current_file)
        elif user_input == 'open':
            record_to_file(transactions, current_file)     
        elif user_input == 'quit':
            break
        else:
            print('You have entered an invalid command. Please try again.')

            
def files_list_update(files_list: list): #updates the list of files 
    """Updates global files_list using data stored in list_of_file.csv when the app starts up"""
    with open('list_of_file.csv', 'r', encoding='utf-8') as list_of_files:
        reader = csv.reader(list_of_files)
        for file_name in reader:
            files_list.extend(file_name)
            
def files_list_write(files_list: list):
    """Writes updated files list into the csv file"""
    with open('list_of_file.csv', 'w', newline= "", encoding='utf-8') as list_of_files:
        writer = csv.writer(list_of_files)
        writer.writerow(files_list)
          
#add a check for if a file already exists with such a name
#add a command to show all files
def create_file(transactions: list):
    #updates the list of files that already exist
    files_list = []
    files_list_update(files_list)
    
    file_name = input('How would you like to name your file? Enter here: ') + '.csv'#for file type
    
    while True:
        if file_name in files_list:#checks if the file already exists
            print("File already exists. Access it through command 'open'.")
            break
        
        current_file = open(file_name, 'w+', encoding='utf-8')
        print(f"Succesfully create a file by the name of {file_name}\n")
        
        #updates the files list
        files_list.append(file_name)
        
        #updates the files list
        files_list_write(files_list)
        
        record_to_file(transactions, current_file)
        break
    
def record_to_file(transactions: list, file: object):     
    transactions_text = ''
    print("""In what order would you like to record transactions?
1 - order in which transactions were made.
2 - ascending by amount.
3 - descending by amount.""")
    
    #loop for user input
    while True:
        user_input = int(input('Enter here: '))
        if user_input == 1:
            transactions_text = transactions_text_list(transactions)
            break
        elif user_input == 2:
            temp_transactions = sorted(transactions,  key=lambda t: t[0], reverse=True)
            transactions_text = transactions_text_list(temp_transactions)
            break
        elif user_input == 3:
            temp_transactions = sorted(transactions,  key=lambda t: t[0], reverse=False)
            transactions_text = transactions_text_list(temp_transactions)
            break
        else:
            print('Invalid command. Enter a number as specified above.')    
    
    with open(file, 'w', newline="", encoding='utf-8') as current_file: #reworked this for csv
        writer = csv.writer(current_file)#created an object to write
        writer.writerow(transactions_text)#wrote data into file 
    #auto closes   
    print('Succsefuly recorded transactions.\n')


#make a helper function for opening a file and writing data into a file
#def write_to_file(file: object, files_list: list, trans_text: str):
    
    
    
    

def transactions_text_list(transactions) -> str:
    """Helper function to get a sorted list of transactions as a string"""
    return f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))