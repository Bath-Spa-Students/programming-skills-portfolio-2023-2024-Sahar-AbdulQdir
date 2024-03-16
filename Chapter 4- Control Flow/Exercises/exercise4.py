#declaring a var with value of the age
Age = 0

#using if statement to see if the age is les than 2
if Age<2 :
    print("This person is a baby")

#using a chain of elif  to select the person's stage of life
elif 4>Age>2 :
    print("This person is a toddler")

elif 13>Age>4 :
    print("This person is a kid")

elif 20>Age>13 :
    print("This person is a teenager")

elif 65>Age>20 :
    print("This person is an adult") 

#using else to select the person's stage of life is elder 
else :
    print("This person is an elder")        