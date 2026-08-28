#Project 9: Bank Transaction Analyzer

transactions = [500, -200, 1000, -300, 750, -150, 400]

types = ["Deposit", "Withdraw", "Deposit", "Withdraw","Deposit", "Withdraw", "Deposit"]

#Q1. Find the total amount deposited and Find the total amount withdrawn.

total_dep=0
total_withdraw=0
for i in transactions:
    if i>0:
        total_dep+=i
    else:
        total_withdraw+=i    

print(f"total deposite amount is :{total_dep}\n total withdraw amount is :{total_withdraw}")

#Q2. Find the final balance after all transactions.

total_tra=0
for i in transactions:
    total_tra+=i

print(f"total transaction amount is :{total_tra}")

#Q3. Find how many deposit were made  and alos how many withdrawals were made.

total_summit_amount=0
total_debit_amount=0

for i in types:
    if i=="Deposit":
        total_summit_amount+=1
    else:
        total_debit_amount+=1

print(f"total  deposit wew made is :{total_summit_amount}\ntotal withdrawals were made is :{total_debit_amount}")            

#Q4. Find the largest deposit amount and also find the largest withdrawal amount

lar_dep=0
lar_withdraw=0

for i in transactions:
    if i>lar_dep:
        lar_dep=i
    if i<lar_withdraw:
        lar_withdraw=i

print(f"the largest deposite amount  is :{lar_dep}\n the largest withdraw amount  is :{lar_withdraw} ")

#Q5. Create a list containing all withdrawal amounts.

res=[]
for i in transactions:
    if i<0:
        res.append(i)

print(f"all the withdrawal amount is :{res} ")        

#Q6. Create a list containing the transaction types where the amount was 500 or more.

res_1=[]
for trs,typ in zip(transactions,types):
    if trs>=500:
        res_1.append(typ)

print(f"the transaction types where the amount was 500 or more is :{res_1}")    

'''Q10. Give each transaction a status:
Deposit → "Money Added"
Withdraw → "Money Spent"'''

for i in types:
    if i=="Deposit":
        print("Money Added")
    else:
        print("Money Spent")  
