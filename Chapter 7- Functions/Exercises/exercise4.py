#Here I define a function called make_shirt
#This function takes 2 parametres (size & message)
def make_shirt(size="large", message="I love Python"):
#Here I use print to display the parametres into two sentences
    print("The size for this shirt is " + size)
    print("The message printed on this shirt is " + '"' + message + '"')

#Here I called the function with different arguments
make_shirt()
make_shirt(size="medium")
make_shirt("XXXL", "Trust the process.")