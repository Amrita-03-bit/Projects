# Project 13: Bank Account Management System

accounts=[]

#Q1.Create a function create_account()

def create_account():

    Account_holder_name=input("enter a account holder name is:")
    Account_number= int(input("enter aaccount number is:"))
    Initial_balance=int(input("enter a initial balnce is:"))

    return [Account_holder_name,Account_number,Initial_balance]

accounts.append(create_account())
print(accounts)

#Q2.Create a function deposit()

def deposit():

    account_num=int(input("enter a account number :"))
    
    for account in accounts:
        if account_num==account[1]:
            dep_amount=int(input("enter deposit amount :"))
            account[2]=account[2]+dep_amount
            print("total balance after deposite is:", account[2])
            
            
        else:
         print("your account number is incorrect")    
deposit()

#Q3.Create a function withdraw()

def withdraw():

   account_num=int(input("enter a account number:"))

   for account in accounts:
      if account_num==account[1]:
         withdraw_amount=int(input("enter ba withdraw amount:"))
         if withdraw_amount<=account[2]:
            account[2]=account[2]-withdraw_amount
            print(f"total balance after withdraw is :{account[2]}")

         else:
            print("Insufficient balance")   
      else:
         print("your balnk account  number is incorrect")     

withdraw()

#Q4. Create a function check_balance()

def check_balance():

   account_num=int(input("enter a account number:"))

   for account in accounts:
      if account_num==account[1]:
         print("Account holder:", account[0])
         print("Account number:", account[1])
         print("Balance:", account[2])
            
         
      else:
         print("ERROR")

check_balance()

#Q5.Create a function find_account()

def find_account():

   account_num=int(input("enter a account number:"))

   for account in accounts:
        if account_num==account[1]:
           return account

   return "ERROR: Account number is incorrect"    


print(find_account())

#Q6.Use Exception Handling

try:

   account_num=int(input("enter a number :"))
   amount=int(input("enter amount:"))

   print("Account number:",account_num)
   print("Amount:",amount) 

except ValueError:
   print("invalid input! plesr enter only number")

#Q7.use OOP

class Bankaccount:

   def __init__(self,name,account_number,balance):
      self.name=name
      self.account_number=account_number
      self.balance=balance

   def deposite(self,amount):
      self.balance=self.balance+amount

   def withdraw(self,withdraw_amount):
      if self.balance>=withdraw_amount:
         self.balance=self.balance-withdraw_amount
      else:
         print("insufficent amount")   

   def  check_balance(self):
      print("current balnce is :",self.balance)

Account=Bankaccount("amrita",111,2222)
Account.deposite(10000)
Account.withdraw(200)
Account.check_balance()

#Q8. Create Multiple Objects

class Bankaccounts:

     def __init__(self,name,account_number,balance):
           self.name=name
           self.account_number=account_number
           self.balance=balance

account1=Bankaccounts("aman",11,234)        
account2=Bankaccounts("rahula",12,345)
account3=Bankaccounts("harsh",13,567)   

print("Account 1:")
print("Name:", account1.name)
print("Account Number:", account1.account_number)
print("Balance:", account1.balance)

print("\nAccount 2:")
print("Name:", account2.name)
print("Account Number:", account2.account_number)
print("Balance:", account2.balance)

print("\nAccount 3:")
print("Name:", account3.name)
print("Account Number:", account3.account_number)
print("Balance:", account3.balance)
      
        

        



   
