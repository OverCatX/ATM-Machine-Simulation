class BankAccount:

    def __init__(self, account_number: int, account_holder: str, account_balance: float):
        self._account_number = account_number
        self._account_holder = account_holder
        self._account_balance = account_balance

    def getNumber(self) -> int:
        return self._account_number

    def getHolder(self) -> str:
        return self._account_holder

    def getBalance(self) -> float:
        return round(self._account_balance, 2)

    def deposit(self, amount) -> None:
        if amount <= 0:
            print('Please type positive integer')
        self._account_balance += amount
        print(f'Deposit successful! Your new balance is: {self.getBalance()}')

    def withdraw(self, amount) -> None:
        if amount < self.getBalance():
            print(f'Insufficient balance to withdraw')
        self._account_balance -= amount
        print(f'Withdrawal successful! Your new balance is: ${self.getBalance()}')

