from threading import RLock

class Account:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = RLock()

    def deposit(self, amount: int) -> bool:
        self.lock.acquire()
        try:
            self.balance += amount
        finally:
            self.lock.release()
        return True
    
    def withdraw(self, amount: int) -> bool:
        self.lock.acquire()
        try:
            if self.balance < amount:
                return False
            self.balance -= amount
        finally:
            self.lock.release()
        return True

class Bank:

    def __init__(self, balance: List[int]):
        self.store = {i + 1: Account(m) for i, m in enumerate(balance)}
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.store or account2 not in self.store:
            return False
        if self.store[account1].withdraw(money):
            return self.store[account2].deposit(money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.store:
            return False
        return self.store[account].deposit(money)

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.store:
            return False
        return self.store[account].withdraw(money)


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)