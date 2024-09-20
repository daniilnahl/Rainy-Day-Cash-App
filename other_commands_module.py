def show_transactions(type_of_command: str,transactions: list):
    transactions_showcase = f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions))
    
    if type_of_command == 'delete':
        print(f'CHOOSE TRANSACTION TO DELETE\n{transactions_showcase}')
    elif type_of_command == 'transactions':
        print(f'VIEWING ALL TRANSACTIONS\n{transactions_showcase}')


def delete_transaction(transactions):
    return 1