#class to create bank account

class Bank_Account:
    def _init_(self):
        self.balance=0
        
    def customer_details(self):
        name='Daniel Wainaina'
        print("Hello",name)
        acc_no=4859285728
        print("Account number: ",acc_no)
        date_of_opening=(input("Enter date of opening: "))
        print("Date of opening is:",date_of_opening)
        self.balance=0
        print("Current balance: ", self.balance,"\n")
        
    def deposit(self):
        amount=int(input("Enter amount to be deposited:"))
        self.balance=+amount
        print("Amount deposited :", amount)
    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if (self.balance>=amount):
            self.balance-=amount
            print("You withdrew:", amount)
        else:
            print("Insufficient balance ")
    def check_balance(self):
        print("Current balance is:", self.balance)
     
B=Bank_Account()

B.customer_details()
B.deposit()
B.withdraw()
B.check_balance()

            
