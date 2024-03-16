#inserting a list and  a several dictionaries
Pets = []
pet_info = {"animal" : "dog",
        "owner" : "Jack",
        "color" : "brown",
        "age" : "7 years"}

#including the list in the dictionary by using append
Pets.append(pet_info)
        
pet_info = {"animal" : "cat",
        "owner" : "Marry",
        "color" : "black & white",
        "age" : "1 year"}

#including the list in the dictionary by using append
Pets.append(pet_info)

pet_info = {"animal" : "rabbit",
        "owner" : "Wennie",
        "color" : "white",
        "age" : "6 months"}

#including the list in the dictionary by using append
Pets.append(pet_info)

pet_info = {"animal" : "bird",
        "owner" : "John",
        "color" : "green",
        "age" : "2 months"}

#including the list in the dictionary by using append
Pets.append(pet_info)

pet_info = {"animal" : "hamster",
        "owner" : "Layla",
        "color" : "brown & white",
        "age" : "2 years"}

#including the list in the dictionary by using append
Pets.append(pet_info)

#now i can easliy give the print order
for pet_info in Pets:
    print("\n This is all I know about" + " " + pet_info["owner"].title() + "'s pet")
    for key, value in pet_info.items() :
        print("\t" + key + ":" + str(value))

