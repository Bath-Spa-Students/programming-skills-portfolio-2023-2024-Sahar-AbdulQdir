#inserting a dictionary
rivres_countries = {"The Thames":"England",
                    "The Murray River":"Australia",
                    "The Saint Lawrence River":"Canada",}

#printing a massege about each river
word = "The Thames"
print(word.title() + " " + "measures 346 kilometers in length and drains into the North Sea.")
word = "The Murray River"
print(word.title() + " " + "provides water for roughly 1.5 million homes across Australia")
word = "The Saint Lawrence River"
print(word.title() + " " + "was historically important for providing passage for European explorers who first visited North America")

print("\n")

#printing the values (rivers name)
for word in rivres_countries :
    print(word.title())

print("\n")

#printing the keys (countries)
for word in rivres_countries :
    print(rivres_countries[word])  