from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, number:int, balance=0):
        self.number = number 
        self.balance = balance 
        self._transactions = []
    
    @abstractmethod
    def account_deposit(self, amount:int):
        pass

    @abstractmethod
    def withdraw(self, amount:int):
        pass

    def get_balance(self):
        return f"Balance: {self.balance:.2f}"

    def __str__(self) -> str:
        return f"{self.number} : {self.balance: .2f}"


class CheckingAccount(Account):
    def __init__(self, number: int, balance=0, min_amount=100000):
        super().__init__(number, balance)
        self.min_amount = min_amount
    
    def account_deposit(self, amount:int):
        self.balance += amount
        self._transactions.append(amount)

    def withdraw(self, amount:int):
        if self.balance - amount >= self.min_amount:
            self.balance -= amount
            self._transactions.append(-amount)
        else:
            print("Insufficient funds")
    
    def __str__(self) -> str:
        return f"Checking Account, Number: {self.number}, Balance: {self.balance:.2f}"


class SavingAccount(Account):

    def __init__(self, number: int, balance=0, min_amount=100000):
        super().__init__(number, balance)
        self.min_amount = min_amount

    def account_deposit(self, amount):
        self.balance += amount
        self._transactions.append(amount)

    def withdraw(self, amount):
        if self.balance - amount >= self.min_amount:
            self.balance -= amount
            self._transactions.append(-amount)
        else:
            print("Insufficient funds")

    def ratio_calculation(self):
        total_deposit = sum([transaction for transaction in self._transactions if transaction>0])
        total_withdraw = sum([transaction for transaction in self._transactions if transaction<0])
        ratio = total_deposit / total_withdraw
        return ratio if total_withdraw != 0 else "No withdraw made"
     
    def __str__(self) -> str:
         return f"Saving Account, Number: {self.number}, Balance: {self.balance}"


class CurrencyAccount(Account):

    exchange_rate = 0.00002 #dollar = 500000 rials

    def __init__(self, number: int, balance=0, min_amount=100000):
        super().__init__(number, balance)
        self.min_amount = min_amount

    def account_deposit(self, amount):
        self.balance += amount
        self._transactions.append(amount)

    def withdraw(self, amount):
        if self.balance - amount >= self.min_amount:
            self.balance -= amount
            self._transactions.append(-amount)
        else:
            print("Insufficient funds")

    @staticmethod
    def convert_to_dollar(rials):
        return rials * CurrencyAccount.exchange_rate

    def display_transactions_in_dollar(self):
        transaction_in_dollar = [transaction * CurrencyAccount.exchange_rate for transaction in self._transactions]
        return transaction_in_dollar

    def __str__(self) -> str:
        return f"Currency Account, Number: {self.number}, Balance: {self.balance}"

    
checking = CheckingAccount("12345", 500000)
checking.account_deposit(200000)
checking.withdraw(100000)
print(checking.get_balance())
print(checking)

saving = SavingAccount("45678", 300000)
saving.account_deposit(250000)
saving.withdraw(100000)
print(saving.get_balance())
print(saving)    
print(saving.ratio_calculation())

currency = CurrencyAccount("67890", 450000)
currency.account_deposit(200000)
currency.withdraw(250000)
print(currency)
print(currency.convert_to_dollar(450000))
print(currency.display_transactions_in_dollar())
