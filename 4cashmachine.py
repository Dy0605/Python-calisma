dy_account = {
    'name': 'dy',
    'password': 123,
    'account_number': '123456',
    'balance': 3000,
    'overdraft': 2000
}

def withdraw(account):
    password_check = int(input('Hello, please enter your password: '))
    if password_check == dy_account['password']:
        print(f"Hello {account['name']}, you are operating on account number {account['account_number']}.")
        amount = int(input('How much money do you want to withdraw? amount = '))

        if account['balance'] >= amount:
            account['balance'] -= amount
            print('You can withdraw your money.')
        else:
            total = account['balance'] + account['overdraft']

            if total >= amount:
                use_overdraft = input('Use overdraft? (y/n)')

                if use_overdraft == 'y':
                    amount_to_use_overdraft = amount - account['balance']
                    account['balance'] = 0
                    account['overdraft'] -= amount_to_use_overdraft
                    print('You can withdraw your money.')
                elif use_overdraft == 'n':
                    print(f"You have {account['balance']} in your account and {account['overdraft']} in your overdraft.")
                else:
                    print('Invalid operation.')
            else:
                print('Insufficient balance, sorry.')
    else:
        print('Incorrect password. Please try again.')

def deposit(account):
    password_check = int(input('Hello, please enter your password: '))
    if password_check == dy_account['password']:
        print(f"Hello {account['name']}, you are operating on account number {account['account_number']}.")
        amount = int(input('How much money do you want to deposit? amount = '))
        account_choice = input("Which account do you want to deposit to? balance = '1', overdraft = '2' ")

        if account_choice == '1':
            account['balance'] += amount
        elif account_choice == '2':
            account['overdraft'] += amount
        else:
            print('Invalid operation')
    else:
        print('Incorrect password. Please try again.')

def check_balance(account):
    print(f"You have {account['balance']} in your account and {account['overdraft']} in your overdraft.")

deposit(dy_account)
print('*******************************')
check_balance(dy_account)