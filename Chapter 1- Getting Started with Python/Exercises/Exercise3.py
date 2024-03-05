#Solution:
#First I'll use the (import) statement to bring the function that defined the current date and time which is (datetime)
import datetime
# Now I am saving the output of the line above in a variable called current_datetime
current_datetime = datetime.datetime.now()
# Then I'll give the program a print command including text,
# which informs users that the content will be written is the current date.
# I also used strftime to transfer the output into string first, 
# so the print statement can define it.
# These symbols (%y / %m / %d) define year,month, and day.
print ("The current date is:" + current_datetime.strftime(" %y / %m / %d "))

# Then I'll give the program another print command including a text,
# which informs users that the content will be written is the current time
# I also used strftime to transfer the output into string first,
# so the print statement can define it.
# These symbols (%H / %M / %S) are defining hours,minutes, and seconds.
print ("The current time is:" + current_datetime.strftime (" %H / %M / %S"))