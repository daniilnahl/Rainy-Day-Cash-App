def show_transactions(transactions):
    print(f'\n'.join(f'{index + 1}. {transaction}' for index, transaction in enumerate(transactions)))

def delete_transaction(transactions):
    return 1