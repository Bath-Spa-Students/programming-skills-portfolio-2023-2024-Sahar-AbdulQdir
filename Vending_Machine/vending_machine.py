print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕊.𝔸.𝕄 𝕍𝕖𝕟𝕕𝕚𝕟𝕘 𝕄𝕒𝕔𝕙𝕚𝕟𝕖 ☙❦")
#importing a library to style tables
from tabulate import tabulate
#importing time function to use ut to delay messeges appearance
from time import sleep

#Defining A table for the drinks
Drinks = [
    ["Drink" , "Price" , "Code"],
    ["Hot Chocolate" , "$5" , "111"],
    ["Apple Juice" , "$4" , "112"],
    ["Water" , "$0.5" , "113"],
    ["Pepsi" , "$1.5" , "114"],
    ["Milk" , "$2" , "115"],
    ["Coffee" , "$1.5" , "116"],
    ["Black Tea" , "$1" , "117"],
    ["Smoothie" , "$8" , "118"]
]

#Printing the item tables for Drinks
print("\t Drinks🥤")
print(tabulate(Drinks[1:], headers=Drinks[0], tablefmt="fancy_grid"))

#Defining A table for the Snacks
Snacks = [
    ["Snack" , "Price" , "Code"],
    ["Oreo" , "$1.5" , "121"],
    ["Muffin Cake" , "$2" , "122"],
    ["Mars" , "$1.75" , "123"],
    ["Apple Pie" , "$1.75" , "124"],
    ["Gum" , "$1.75" , "125"],
    ["Sliced Pineapples" , "$0.75" , "126"],
    ["Biscuit" , "$1" , "127"],
    ["Cookies" , "$2" , "128"]
]

#Printing the item tables for Snacks
print("\t Snacks🍫")
print(tabulate(Snacks[1:], headers=Snacks[0], tablefmt="fancy_grid"))

#Creating empty list to store selected items later
Cart = []

#This is a loop for selecting items with a chain of if statement to suggest related products
while True:
#Taking input from the user
    code = input("Enter the code of the item you wish to add it to your cart, Or type 'done' to continue paying: ")
    if code == "111":
     print("Hot chocolate id often bought with Muffin Caka!!, Code=112")

    elif code == "112":
       print("Apple Pie would be a great choice if you add it to your juice, Code=124")

    elif code == "113":
       print("Water often bought with gum, Code=125")
    
    elif code == "114":
       print("Pepsi is often bought with Mars chocolate, Code=123")

    elif code == "115":
       print("Oreo is the Milk bestfriend, Code=121")
    
    elif code == "116":
       print("Cookies is a great choice with coffee , Code=128")

    elif code == "117":
       print("Tea is often bought with biscuit, Code=127")

    elif code == "118":
       print("There is no smoothie without Sliced Pineapples, Code=126")

#Checking if the user is done from selecting
    if code.lower () == "done":
       break

#Searching for an item in both tables (Drinks & Snacks)
    for item in Drinks[1:]:
      if code == item[2]:
        print(f"You've selected: {item[0]} \n Price is:{item[1]}")
        Cart.append(item)
        break
    else:
     for item in Snacks[1:]:
         if code == item[2]:
            print(f"You've selected: {item[0]} \n Price is:{item[1]}")
            Cart.append(item)
            break
#Displaying a message that says item id not found when the user inputs a code that does not exsist
     else:
       print("Item not found✖️")

#Calculate Total amount
Total = sum (float(item[1].replace("$" , "")) for item in Cart)

#Displaying a table like a billing system
print("\nBill🧾:")
print(tabulate(Cart , headers=["Item" , "Price" , "Code"], tablefmt="rst"))

#Displaying the total amount
print(f"Total is: ${Total}")

#This is an input for inserted money
Money_inserted = float(input("Enter the amount of money you inserted: $"))

#Checking if the inserted money is enough
if Money_inserted < Total:
   print("Insufficient credit.")

else:
   Change = Money_inserted - Total
   print(f"Money inserted: ${Money_inserted}.")
   print(f"Your will receive ${Change} as a change.")


if Money_inserted >= Total:
#Delaying the messeges to display after few seconds so it will be like the machine is proccesing 
  Seconds_1 = 2
  sleep(Seconds_1)
  print("Your items have been displayed✅")
  Seconds_2 = 2.5
  sleep(Seconds_2)
  print("Your change has been displayed✅")

