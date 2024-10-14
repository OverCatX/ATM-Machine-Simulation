import json
from BankAccount import BankAccount


class Atm:

    def __init__(self, account_data='accounts.json'):
        self.data = None
        self.account_data = account_data
        self.accounts = self.load_data()

    def load_data(self):
        try:
            with open(self.account_data, 'r') as data:
                return json.load(data)
        except FileNotFoundError:
            return {}

    def saveData(self):
        with open(self.account_data, 'w') as data:
            json.dump(self.account_data, data)

    def createAccount(self, acc_number, acc_holder, acc_pin) -> None:
        if acc_number in self.accounts:
            print('This account has exists')
        self.accounts[acc_number] = {
            'holder': acc_holder,
            'pin': acc_pin,
            'balance': 0
        }
        self.saveData()
        print(f"Account's number: [{acc_number}] has been created.")

    def authenticate(self, acc_number, acc_pin) -> None:
        if acc_number not in self.accounts:
            print(f"Account's number [{acc_number}] doesn't exists.")
            return
        if self.accounts[acc_number]['pin'] != acc_pin:
            print(f'Password not correct.')
            return
        self.management_menu()
        self.data = {'acc_number': acc_number,
                     'acc_holder': self.accounts[acc_number]['holder'],
                     'acc_pin': acc_pin,
                     'acc_balance': self.accounts[acc_number]['balance']}
        print(f'Logged in..')

    def management_menu(self):
        print('Welcome to Management Menu'
              '\nChoose choice here:'
              '\n1.Deposit'
              '\n2.Withdraw'
              '\n3.Close Bank Account'
              '\n4.Exit')
        choice = int(input('Enter your chocie: '))
        if choice == 1:
            amount = float(input('Enter amount to deposit: '))
            if amount <= 0:
                print('Please enter positive number.')
                return
            bankAccount = BankAccount(self.data['acc_number'],
                                      self.data['acc_holder'],
                                      self.data['acc_pin'],
                                      self.data['acc_balance'])
            bankAccount.deposit(amount)
            self.accounts[self.data['acc_number']]['balance'] = bankAccount.getBalance()
            self.saveData()
        elif choice == 2:
            amount = float(input('Enter amount to withdraw: '))
