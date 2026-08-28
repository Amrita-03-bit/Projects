#Project 7: Product Sales Analyzer

products = ["Laptop", "Phone", "Tablet", "Watch", "Earbuds", "Camera"]

prices = [55000, 25000, 18000, 5000, 3000, 40000]

sold_quantity = [2, 5, 3, 8, 10, 1]

#Q1. Find the total sales amount for each product.

total_sales=[]
for product,price,quantity in zip(products,prices,sold_quantity):
    cost=price*quantity
    total_sales.append(cost)
    print(product,"=",cost)

#Q2. Find the total revenue from all products.

total_products=0
for i in total_sales:
    total_products+=i
print(f"total renvenue from all products : {total_products}")    

#Q3. Find the product that generated thr highest renvenue and lowest renvenue Print its name and revenue 

high_ren=total_sales[0]
high_pro=products[0]
low_pro=products[0]
low_ren=total_sales[0]
for product,price,quantity in zip(products,prices,sold_quantity):
    cost = price * quantity
    if cost>high_ren:
        high_ren=cost
        high_pro=product
    if cost<low_ren:
        low_ren=cost
        low_pro=product
print(f"high revenue  products is {high_pro} and high revenue is :{high_ren}\n low revenue product is:{low_pro} and low revenue is :{low_ren}")        

#Q4. Find how many products have a price greater than ₹10,000.

count_pro=0
for i in prices:
    if i>10000:
        count_pro+=1
print(f"total no of products greater than 10000 is :{count_pro}")        

#Q5. Print the names of products that sold 5 or more units.

res=[] 
for product,price,quantity in zip(products,prices,sold_quantity):
    if quantity>=5:
        res.append(product)
print(f"names of products that sold 5 or more units is :{res}")        

#Q6. Find the average number of units sold.

count_sold=0
for i in sold_quantity:
    count_sold+=i
average=count_sold/len(sold_quantity)
print(f"average of sold quantity is :{average}")    

#Q7. Find how many products sold more units than the average units sold.

res_1=[]
for product,price,quantity in zip(products,prices,sold_quantity):
    if quantity>average:
        res_1.append(product)
print(f"products sold more units than the average units sold is :{res_1}")        

#Q8. Create a list containing the names of products whose revenue is ₹50,000 or more.

res_2=[]
for product,price,quantity in zip(products,prices,sold_quantity):
    cost=price*quantity
    if cost>=50000:
        res_2.append(product)
print(f"names of products whose revenue is ₹50,000 or more is :{res_2}")

'''Q10. Give each product a sales category:
Revenue ₹1,00,000 or more → "Excellent Sales"
Revenue ₹50,000–₹99,999 → "Good Sales"
Revenue ₹20,000–₹49,999 → "Average Sales"
Revenue below ₹20,000 → "Low Sales"'''

for product,price,quantity in zip(products,prices,sold_quantity):
    cost=price*quantity
    if cost>=100000:
        print(product,"Excellent sales")
    elif cost>=50000 :
        print(product,"Good Sales")
    elif cost>=20000:
        print(product,"Average Sales")
    else:
        print(product,"Low Sales")            