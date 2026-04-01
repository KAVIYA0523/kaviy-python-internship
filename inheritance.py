# Parent class
class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display(self):
        print("Account No:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


# Child class 1
class SavingsAccount(Account):
    def __init__(self, acc_no, name, balance, interest):
        super().__init__(acc_no, name, balance)
        self.interest = interest

    def show_interest(self):
        print("Interest Rate:", self.interest)


# Child class 2
class CurrentAccount(Account):
    def __init__(self, acc_no, name, balance, min_balance):
        super().__init__(acc_no, name, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Cannot withdraw! Minimum balance required.")
        else:
            self.balance -= amount
            print("Withdraw successful. Remaining balance:", self.balance)


# Create objects
s1 = SavingsAccount(101, "Kaviya", 5000, 5)
s1.display()
s1.show_interest()

print("-----")

c1 = CurrentAccount(102, "Kaviya", 3000, 1000)
c1.display()
c1.withdraw(2500)