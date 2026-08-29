#Project 11: Mini Shopping Cart

products = ["Laptop", "Mouse", "Keyboard", "Headphones", "USB Cable"]

prices = [55000, 800, 1500, 2500, 400]

#Q1. Display all products with their prices.

for pro,pric in zip(products,prices):
    print(pro,"=",pric)

#Q2.Ask the user to enter the product number and  qunatity and then total cost of the selected product and then whether they want to add another product and after  Calculate the total bill of all selected products and discount 10%


pro_num_1=int(input("Enter the selcted products number is:"))
quantity_num=int(input("Enter the quantity :"))

price=prices[pro_num_1-1]
cost=price*quantity_num

print(f"total cost of the selected products is :{cost}")    

add_pro = input("Do you want to add another product? yes/no: ")

if add_pro == "yes":

    pro_num_2 = int(input("Enter the product number: "))
    quantity = int(input("Enter the quantity: "))

    price = prices[pro_num_2 - 1]
    cost_2 = price * quantity

    total_bill = cost + cost_2

else:
    total_bill = cost

print(f"Total bill of all selected products is: {total_bill}")

if total_bill>=5000:
    discount=total_bill*10/100
    final_bill=total_bill-discount
    
else:
    discount=0
    final_bill=total_bill-discount    

print("final bill is :",final_bill)    

#Q3.Print the shopping summary which we are selected.

print("product:",products[pro_num_1-1])
print("prices:",prices[pro_num_1-1])
print("quantity:",quantity_num)
print("total cost:",cost)

if add_pro == "yes":

    print("\nProduct:", products[pro_num_2 - 1])
    print("Price:", prices[pro_num_2 - 1])
    print("Quantity:", quantity)
    print("Total cost:", cost_2)

#Q4.Print the final shopping bill.

print(f"totall bill of buy product is :{total_bill}\n total discount is :{discount}\n final bill is {final_bill}")

