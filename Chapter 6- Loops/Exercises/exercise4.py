#This is a list
sandwich_orders = ["tuna", "cheese", "beef", "fries"]
#This is an empty list
finished_sandwich = []

#Processing each sandwich order
while sandwich_orders :
#Here I use pop to get the next sandwich order
    sandwich = sandwich_orders.pop()
#Here I use print to tell the user that the sandwichs are under preperation
    print("We are preparing your " + sandwich +  " sandwich")
#Here I added the prepared sandwich to the finished sandwiches list
    finished_sandwich.append(sandwich)

#Here I print the message for each finished sandwich
for sandwich in finished_sandwich:
    print("\n We just made your " + sandwich + " sandwich")