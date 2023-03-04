#class to bank account with input prompt

class Bank_Account:
    def _init_(self):
        self.balance=0
        
    def customer_details(self):
        customer_name=(input("Enter your name: "))
        account_number=(int(input("Enter Your account number: ")))
        date_of_opening=(input("Enter date of opening : "))
        self.balance=0
        print("\nHello",customer_name)
        print("Your account number is:",account_number)
        print("Date of opening is:",date_of_opening)
        print("Current balance: ", self.balance)
        
    def deposit(self):
        amount=int(input("Enter amount to be deposited:"))
        self.balance=+amount
        print("Amount deposited :", amount)
    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if (self.balance>=amount):
            self.balance-=amount
            print("You withdrew:", amount,"\n")
        else:
            print("Insufficient balance ,","\n")
    def check_balance(self):
        print("Current balance is:", self.balance)
    
      
B=Bank_Account()
B.customer_details()
B.deposit()
B.withdraw()
B.check_balance()

            