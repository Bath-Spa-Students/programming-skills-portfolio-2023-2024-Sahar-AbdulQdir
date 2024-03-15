#daclaring a var that has a list in it
invitees = ["Mom", "Dad", "brother Abdullah", "sister Sarah", "friend Ruba", "Grandma Sua'ad"]

#printing a massege to each item on the list
print("Hi" + " "+ (invitees[0]) + "," + " " + "I would like to invite you to dinner this Monday.")
print("Good morning" + " "+ (invitees[1]) + "," + " " + "We're having a dinner this Monday and I really want to be with us")
print("Hello" + " "+ (invitees[2]) + "," + " " + "I was wondering if you could come to have dinner with us this Monday") 
print("Hi" + " "+ (invitees[3]) + "," + " " + "don't forget to come to the dinner this Monday")
print("Hi" + " "+ "my" + " " + (invitees[4]) + "," + " " + "you should come to the dinner this Monday")
print("Good evening" + " "+ (invitees[5]) + "," + " " + "I hope yo're doing good, I would like to invite you to have a dinner with the family this Monday")

print("\n")

#printing the name of the guest who is nit coming
print("Unfortionately," + " " + (invitees[3]) + " " + "Can't come to the dinner")

print("\n")

#replacing the guest who couldn't come with the new one
invitees[3] = "Uncle Sami"

print("This is the updated list:")

print("\n")

print("Hi" + " "+ (invitees[0]) + "," + " " + "I would like to invite you to dinner this Monday.")
print("Good morning" + " "+ (invitees[1]) + "," + " " + "We're having a dinner this Monday and I really want to be with us")
print("Hello" + " "+ (invitees[2]) + "," + " " + "I was wondering if you could come to have dinner with us this Monday") 
print("Hi" + " "+ (invitees[3]) + "," + " " + "don't forget to come to the dinner this Monday")
print("Hi" + " "+ "my" + " " + (invitees[4]) + "," + " " + "you should come to the dinner this Monday")
print("Good evening" + " "+ (invitees[5]) + "," + " " + "I hope yo're doing good, I would like to invite you to have a dinner with the family this Monday")