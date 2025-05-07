class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Your balance has been replenished by {amount}$')
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount}$ have been withdrawn from your account')
        else:
            print(f'Insufficient funds. Only {self.balance}$ available')

    def __str__(self):
        return f'Account: {self.account_number}. Balance: {self.balance}$'


if __name__ == '__main__':
    acc = BankAccount('1234 5678 91011 1213', 100)
    print(acc)
    acc.deposit(100)
    print(acc)
    acc.withdraw(300)
    acc.withdraw(150)
    print(acc)
