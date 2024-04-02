#This is a list
sandwich_orders = ["tuna", "pastrami", "cheese","pastrami", "beef", "fries", "pastrami"]
#This is an empty list
finished_sandwich = []

#Here I print a massege to tell the user that the pastrami sandwich are not available 
print("We're sorry, we dont have " + (sandwich_orders[1]) + " sandwich for today" )

#Here I removed all the pastrami from the sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

#Processing each sandwich order
while sandwich_orders:
#Here I use pop to get the next sandwich order
    the_sandwich = sandwich_orders.pop()
##Here I use print to tell the user that the sandwichs are under preperation
    print("\nWe are working on your " + the_sandwich + " sandwich")
#Here I added the prepared sandwich to the finished sandwiches list
    finished_sandwich.append(the_sandwich)

    for sandwich in finished_sandwich:
#Here I print the message for each finished sandwich
        print("\nI made a " + sandwich + " sandwich")