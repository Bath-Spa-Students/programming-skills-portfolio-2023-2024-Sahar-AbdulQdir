#Here I define a function called describe_city
#This function takes 2 parametres (City & Country)
def describe_city(City, Country="Chile"):
    message = City.title() + " is located in " + Country.title()
#Here I use print to display the parametres in a sentence
    print(message)


#Here I called the function with different arguments
describe_city("Tocopilla")
describe_city("Angol")
describe_city("Madani", "Sudan")
describe_city("Cairo", "Egypt")