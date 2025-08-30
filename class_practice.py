# Logic 

class BankAccount :
    def __init__(self , owner , balance = 0.0):
        self.balance = balance
        if balance < 0 :
            raise ValueError ("Balance must be > 0")
        self.owner = owner 
        self.balance = balance 
    def acc_info(self):
        Balance_format = f"{self.balance:,.0f}".replace("," , ".")
        return f"Owner : {self.owner} , Balance : {Balance_format} VNÐ"
# User interact
acc_name = input("Name : ")
acc_balance = float(input("Balance : "))


# Program launch 
acc = BankAccount(acc_name , acc_balance)
print(acc.acc_info())