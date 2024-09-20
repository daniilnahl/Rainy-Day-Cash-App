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
        try: #keeps prompting user to enter a valid label for a transaction to be deleted
            delete_transaction = int(input('Enter numbered label: '))
            transaction_index = delete_transaction - 1
            print(f"Succesfully deleted transaction {delete_transaction}. {transactions[transaction_index]}\n")
            del transactions[transaction_index]
            break
        except ValueError:
            print(f"You have entered an invalid label value. You can only enter an integer such as '1'")
    #add a check for if a transaction exists, add a check if a user is entering a integer non decimal for the "labeled transaction"