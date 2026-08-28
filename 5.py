# Project 5: Shopping Cart Analyzer

items = ["Laptop", "Mouse", "Keyboard", "Headphones", "USB Cable"]
prices = [55000, 800, 1500, 2500, 400]
quantities = [1, 2, 1, 2, 3]

def shopping_analyzer(items, prices, quantities):

    #Q1. Find the total cost of each item.   
    
    total_cost=[]
 
    for i in range(len(items)):
        cost=prices[i]*quantities[i]
        total_cost.append(cost)
        print(items[i],"=",cost)

    # Q2 Find the total bill of all items.

    total_bill=0
    for i in prices:
        total_bill+=i
    print("total bill is :",total_bill)   

    # Q3. Find the name of the most expensive item based on its price.
    # Print the item name and its price.

    most_expension=prices[0]
    costly_item=0
    for index,item in enumerate(prices):
        if item>most_expension:
            most_expension=item
            costly_item=index
    print("most expension items is :",items[costly_item],"and they prices is :",most_expension)    

    # Q4. Find the name of the item whose total cost (price × quantity) is highest.
    # Print the item name and its total cost.

    highest_total_cost = prices[0] * quantities[0]
    highest_item = items[0]
    for i in range(len(prices)):
        total_cost=prices[i]*quantities[i]
        if total_cost>highest_total_cost:
            highest_total_cost=total_cost
            highest_item=items[i]
    print(f"highest total cost in items is:{highest_item}\n highest total cost is:{highest_total_cost}")

    # Q5. Find how many items have a price greater than 1000 and Print the names of items whose price is less than 2000.
    # Apply a discount rule:
        # If the total bill is 5000 or more → give 10% discount.
        # Otherwise → no discount.
        # Print the discount amount and final bill.
    
    total_greater_item=0
    less_item_name=[]
    for i in range(len(prices)):
        if prices[i]>1000:
            total_greater_item+=1
        if prices[i]<2000:
            less_item_name.append(items[i])
        if total_bill>=5000:
            discount=(total_cost*10)/100
            final_bill=total_bill-discount
        else:
            discount=0
            final_bill=total_bill         


    print(f"total item greater than 1000 is :{total_greater_item}\nitem names whose pices less than 2000 is:{less_item_name}\nfinal bill is :{final_bill}")  

    # Q6.find  the names of item whose quantity is 2 or more.
   
    result=[]
    for item,quantity in zip(items,quantities):
        if quantity>=2:
          result.append(item)
    print("Items with quantity 2 or more:", result)    

    #Q7. find the item with the lowest total cost  Print the item name and total cost.
    lower_total_cost=prices[0]*quantities[0]
    lower_item=items[0]
    for item,price,quantity in zip(items,prices,quantities):
        total_cost=price*quantity
        if total_cost<lower_total_cost:
            lower_total_cost=total_cost
            lower_item = item
    print(f"Lowest cost item is:{lower_item}\n Lowest total cost is:{lower_total_cost}")

    '''Q8. Create a function that prints a shopping summary:**
         Item name,Price,Quantity,Total cost,for every item.'''
    
    total_cost=prices[0]*quantities[0]
    for item, price, quantity in zip(items, prices, quantities):
      total_cost = price * quantity
      print("Item:", item)
      print("Quantity:", quantity)
      print("Price:", price)
      print("Total cost:", total_cost)
      print("--------------------")

items = ["Laptop", "Mouse", "Keyboard", "Headphones", "USB Cable"]
prices = [55000, 800, 1500, 2500, 400]
quantities = [1, 2, 1, 2, 3]

shopping_analyzer(items, prices, quantities)