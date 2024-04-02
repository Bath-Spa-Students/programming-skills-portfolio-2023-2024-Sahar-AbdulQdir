#daclaring a var that has a list in it
invitees = ["Mom", "Dad", "brother Abdullah", "sister Sarah", "friend Ruba", "Grandma Sua'ad"]
#printing a massege to each item on the list
print("Hi" + " "+ (invitees[0]) + "," + " " + "I would like to invite you to dinner this Monday.")
print("Good morning" + " "+ (invitees[1]) + "," + " " + "We're having a dinner this Monday and I really want to be with us")
print("Hello" + " "+ (invitees[2]) + "," + " " + "I was wondering if you could come to have dinner with us this Monday") 
print("Hi" + " "+ (invitees[3]) + "," + " " + "don't forget to come to the dinner this Monday")
print("Hi" + " "+ "my" + " " + (invitees[4]) + "," + " " + "you should come to the dinner this Monday")
print("Good evening"+ (invitees[5]) +", I hope yo're doing good, I would like to invite you to have a dinner with the family this Monday")

print("\n")

#print a massege to appologize
print("Unfortionately,\n But I can only invite two people only, I'm so sorry for that")

#removing items from the list
print("I'm sorry" + " " + (invitees[2]) + " " + "But I can't invite you to the dinner this Monday ")
invitees.pop(2)

print("I'm sorry" + " " + (invitees[2]) + " " + "But I can't invite you to the dinner this Monday ")
invitees.pop(2)

print("I'm sorry" + " " + (invitees[2]) + " " + "But I can't invite you to the dinner this Monday ")
invitees.pop(2)

print("I'm sorry" + " " + (invitees[2]) + " " + "But I can't invite you to the dinner this Monday ")
invitees.pop(2)

print("\n")

#print a massege to tell the wo remaining people that they are still invited
print("Hi" + " "+ (invitees[0]) + "," + " " + "You're still invited to the dinner this Monday")
print("Hello" + " "+ (invitees[1]) + "," + " " + "You're still invited to the dinner this Monday")

#deleting the list items
del invitees[0]
del invitees[0]


#printing the empty list
print("This is the updated list after removing the two items left",invitees)
