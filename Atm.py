import json
import math
import random

from BankAccount import BankAccount


def genNumber():
    digits = [i for i in range(0,10)]
    number = ""
    for i in range(6):
        number += str(digits[math.floor(random.random() * 10)])
    return number


class Atm:

    def __init__(self, account_data='accounts.json'):
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
            json.dump(self.accounts, data)

    def createAccount(self, acc_number, acc_holder, acc_pin):
        if acc_number in self.accounts:
            print('This account has exists')
            return False
        self.accounts[acc_number] = {
            'holder': acc_holder,
            'pin': acc_pin,
            'balance': 0
        }
        self.saveData()
        print(f"Account's number: [{acc_number}] has been created.")
        self.atm_menu()
        return True

    def authenticate(self, acc_number, acc_pin):
        if acc_number not in self.accounts:
            print(f"Account's number [{acc_number}] doesn't exists.")
            return False
        if acc_pin != int(self.accounts[acc_number]['pin']):
            print(f'Password not correct.')
            return False
        return BankAccount(acc_number, self.accounts[acc_number]['holder'], acc_pin,
                           self.accounts[acc_number]['balance'])

    def management_menu(self, account):
        while True:
            print(f'\nWelcome {account.getHolder()} to Management Menu'
                  '\nChoose choice here:'
                  '\n1.Deposit'
                  '\n2.Withdraw'
                  '\n3.Check Balance'
                  '\n4.Exit')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                amount = float(input('Enter amount to deposit: '))
                account.deposit(amount)
                self.accounts[account.getNumber()]['balance'] = account.getBalance()
                self.saveData()
            elif choice == 2:
                amount = float(input('Enter amount to withdraw: '))
                account.withdraw(amount)
                self.accounts[account.getNumber()]['balance'] = account.getBalance()
                self.saveData()
            elif choice == 3:
                print(f'Your balance: {account.getBalance()}')
            elif choice == 4:
                print('Thank you for using ATM.')
                break

    def atm_menu(self):
        while True:
            print('\nWelcome to ATM Menu'
                  '\nChoose choice here:'
                  '\n1.Create Bank Account'
                  '\n2.Login'
                  '\n3.Exit')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                acc_holder = input('Enter your name: ')
                acc_pin = int(input('Enter your pin code (6 digits): '))
                if len(str(acc_pin)) == 6:
                    self.createAccount(genNumber(), acc_holder, int(acc_pin))
                else:
                    print('Pin code must be 6 digits'
                          '\n')
            elif choice == 2:
                acc_holder = input("Enter your account's number: ")
                acc_pin = int(input('Enter your pin code (6 digits): '))
                authed = self.authenticate(acc_holder, acc_pin)
                if authed:
                    self.management_menu(authed)
            elif choice == 3:
                print('Thank you for using ATM.')
                break
