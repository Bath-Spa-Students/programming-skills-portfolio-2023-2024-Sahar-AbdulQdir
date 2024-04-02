#Starting an infinite loop
while True:
#see if the user dont want to add topping, the user should write "quit"
   topping = input("enter the toppings you want to add to your pizza, then enter 'quit' to place your order: ")
#if the user enter quit print this massege
   if topping.lower() == "quit":
       print("Your order is preparing!")
# break is used to exit the loop
       break
   else:
#if the user choose the topping, this massege will appear
      print("We will add" + " " + topping + " " + "to your pizza")