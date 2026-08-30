'''🛒 Project 16: Mini Shopping Cart- Create a shopping system to view products, add/remove products, calculate the total bill, and continue or end shopping.'''

shop={  "Laptop" : 50000,
       "Headphones" : 2000,
      "Mouse" : 800,
     "Keyboard" : 1500}
cart=[]
def show():

    
    while True:

      print(shop)

      #Add product
      new_pro=input("enter the product you want to add:").title()
      if new_pro in shop:
         cart.append(new_pro)
      else:
         print("products not found")   

      add_pro=input("you add the product(yes/no):")
      if add_pro=="yes":
         continue
      else:
         print("continue shooping")

       #Remove product 
      pro_remove=input("you remove the product from cart (yes/no):")
      if pro_remove=="yes":
        remove_pro=input("which one product you remove to cart:").title()
        if remove_pro in cart:
         cart.remove(remove_pro)
         print("products remove from cart")
        else:
         print("product not in cart")   
      else :
        print("continuue shopping")  

      #Finall bill
      total_bill=0
      for i in cart:
       total_bill+=shop[i]
      print("finall bill :",total_bill)   

      #Continue shopping
      choice=input("Do you want to continue shopping ?(yes/no):")
      if choice=="yes":
        continue
      else:print("thanking for shopping")
      break

show()