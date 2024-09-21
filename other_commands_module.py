def show_transactions(type_of_command: str,transactions: list):
    transactions_showcase = f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))
    
    if type_of_command == 'delete':
        print(f'CHOOSE TRANSACTION TO DELETE\n{transactions_showcase}')
    elif type_of_command == 'transactions':
        print(f'VIEWING ALL TRANSACTIONS\n{transactions_showcase}')


def delete_transaction(transactions):
    show_transactions('delete',transactions)
    print('Enter the number before the transaction that you would like to delete.')
    while True:
            try: 
                #Prompts user to enter a valid label 
                delete_transaction = int(input('Enter numbered label: ')) 
                #calculates transaction index
                transaction_index = delete_transaction - 1 

                #checks if the transaction_index  is within bounds 
                if transaction_index not in range(len(transactions)): 
                    print("The transaction you want to delete is out of bounds and doesn't exist")
                
                else:
                    print(f"Succesfully deleted transaction {delete_transaction}. {transactions[transaction_index]}\n")
                    del transactions[transaction_index]#deletes the transaction element
                    break
            
            except ValueError:# Handle invalid input that isn't an integer
                 print('Invalid input. Please enter an integer number corresponding to the transaction.')


        
            
   