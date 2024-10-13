
"""Module for handling functions for recording and reading data from and to CSV files."""
import csv

global current_file #file that is being interacted with
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
            current_file = create_file()  
            print(current_file)
        elif user_input == 'record':
            record_to_file(transactions, current_file)     
        elif user_input == 'quit':
            break
        else:
            print('You have entered an invalid command. Please try again.')
            
def files_list_update(): #updates the list of files 
    """Updates global files_list using data stored in list_of_file.csv when the app starts up"""
    with open('list_of_file.csv', 'r', encoding='utf-8') as list_of_files:
        reader = csv.reader(list_of_files)
        for file_name in reader:
            files_list.extend(file_name)
            
        
        
    
    
#add a check for if a file already exists with such a name
#add a command to show all files
def create_file():
    file_name = input('How would you like to name your file? Enter here: ') + '.csv'#for file type
    
    while True:
        if file_name in files_list:#checks if the file already exists
            print('File already exists. Access it through command prompt.')
            break
        
        #intializes the file
        global current_file#without this code it doesnt work
        current_file = open(file_name, 'w+', encoding='utf-8')
        print(f"Succesfully create a file by the name of {file_name}\n")

        #CREATE FILE AND PROMPT TO RECORD INTO IT
        #THE GLOBAL FILE ACCESS IS WHAT CAUSING THE ERROR. IT CAN"T DO THAT.
        #SO, USE FUNCTIONS BELOW IN THIS METHOD.
        #stores the file name
        files_list.append(file_name)
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
    
    with open(file, 'w', newline='\n', encoding='utf-8') as current_file: #reworked this for csv
        writer = csv.writer(current_file)#created an object to write
        writer.writerow(transactions_text)#wrote data into file 
    #auto closes   
    print('Succsefuly recorded transactions.\n')
    
def transactions_text_list(transactions) -> str:
    """Helper function to get a sorted list of transactions as a string"""
    return f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))