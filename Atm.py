import json


class Atm:

    def __init__(self, account_data='accounts.json'):
        self.account_data = account_data
        self.acounts = self.load_data()

    def load_data(self):
        try:
            with open(self.account_data, 'r') as data:
                return json.load(data)
        except FileNotFoundError:
            return {}

    def saveData(self):
        with open(self.account_data, 'w') as data:
            json.dump(self.account_data, data)

    def createAccount(self, acc_number, acc_holder, acc_pin):
        if acc_number in self.acounts:
            print('This account has exists')
        self.acounts[acc_number] = {
            'holder': acc_holder,
            'pin': acc_pin,
            'balance': 0
        }
        self.saveData()
        print(f"Account's number: {acc_number} has been created.")

    def authenticate(self, acc_number, acc_pin):
        
