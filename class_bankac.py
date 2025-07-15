class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # Private variable

      
    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} withdrew ₹{amount:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"BankAccount(owner: {self.owner}, Balance: ₹{self.__balance:.2f})"

bank_account= BankAccount("Anjana",1000)
bank_account.deposite(500)
bank_account.withdraw(200)
bank_account.get_balance()