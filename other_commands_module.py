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
            #keeps prompting user to enter a valid label for a transaction to be deleted
            delete_transaction = int(input('Enter numbered label: ')) 
            #ADD A try here with except value error 


            transaction_index = delete_transaction - 1 #declares the index of the transaction element that would be deleted
            if transaction_index not in range(len(transactions)): #checks if the index of the transaction user wants to delete is in the range of the size of the transactions list 
                print("The transaction you want to delete is out of bounds and doesn't exist")
            else:#deletes the transaction element
                print(f"Succesfully deleted transaction {delete_transaction}. {transactions[transaction_index]}\n")
                del transactions[transaction_index]
                break
        
            
   