# First I'll use the input statement to allow users enter their text.
# And I'll save it in a variable called Radius_of_circle.
# I also used the float word to transfer the text given into Decimal number.
Radius_of_circle = float(input ("enter the radius of your circle "))
#Then I'll use this formula to calculate the area of the circle.
Formula = float( Radius_of_circle  * Radius_of_circle  * 3.14)
#Then I'll use print command including a text,
# to inform users that the written content is the circle's area,
# I also use str to transfer the float data into string data 
#so the print statement could accept it.
print ("The circle area of the radius " + str(Radius_of_circle)+ " is " + str(Formula))
