#Here I start the infinite loop 
while True:
#Here I ask the user to enter their age
    age = input("How old are you, enter 'quit' to exit")
#Here I check if the user want to exit the loop
    if age.lower() == 'quit':
        break
#This is a normal converting to an integer
    age = int(age)
#Here I used a chain of if statement to select the ticket for the price based on the age 
    if age < 3:
        print(" your ticket is for free")
    elif age < 13:
        print(" The price for you ticket is $10")
    else:
        print(" The price for your ticket is $15")