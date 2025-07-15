class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self,amount:float) ->None:
        if amount >0:
            self.__balance += amount
            print(f"{self.owner} deposites rs.{amount:.2f}. New balance is rs.{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} withdrew rs.{amount:.2f}. New balance is rs.{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"BankAccount(owner: {self.owner}, Balance: rs.{self.__balance:.2f})"
        
if __name__ == "__main__":
    acc1 = BankAccount("Anjana", 1000)
    acc2 = BankAccount("Anu", 500)

    # Transactions for Anjana
    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.deposit(1200)
    print(acc1)
    print(f"Final balance (Anjana): ₹{acc1.get_balance():.2f}")
    print()

    # Transactions for Anu
    acc2.withdraw(100)
    acc2.deposit(300)
    acc2.withdraw(800)  
    print(acc2)
    print(f"Final balance (Anu): ₹{acc2.get_balance():.2f}")

