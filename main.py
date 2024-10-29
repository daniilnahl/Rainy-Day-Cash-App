import records_module as rm
import main_module as mm
import other_commands_module as ocm    
import files_module as fm
def main():
    #welcome message with initial view of the commands
    mm.welcome_message()
    mm.command_list()
    
    #variables
    transactions = [[-12.1, '2024-10-14'],[-1.1, '2024-10-14'],[-12.0, '2024-10-14']]  

    while True:
        #updates the total amount of money with each cycle 
        total = mm.total_amount(transactions)

        command = input("Enter the command you would like to do: ").lower()
        print()

        #records a transaction
        if command == 'add':  
            print('You have chosen to record a transaction.')
            rm.record_loop(transactions)

        #deletes a transaction
        elif command == 'delete':
           ocm.mod_or_del_transaction(command, transactions)
           
        #modify a transaction
        elif command == 'modify':
            ocm.mod_or_del_transaction(command, transactions)
        
        #shows total amount stored
        elif command == 'total':
            print(f'Your total is ${total}\n')

        #shows all the recorded transactions
        elif command == 'transactions':
            ocm.show_transactions('transactions', transactions)

        #opens files menu
        elif command == 'files':
            fm.file_menu(transactions)
            mm.command_list()
            
        elif command == 'quit':
            break   

        elif command == 'help':
            mm.command_list()

        else:
            print('You have entered an invalid command. Please try again.\n')
        
if __name__ == "__main__":
    main()