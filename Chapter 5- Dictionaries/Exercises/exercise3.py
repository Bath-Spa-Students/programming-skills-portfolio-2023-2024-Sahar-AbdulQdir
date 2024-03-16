#inserting a dictionary
glossary = {"Integer": "is a whole number, positive or negative, without decimals, of unlimited length.",
            "List": "are used to store multiple items in a single variable.",
            "sys": "is used to check the Python version of the editor",
            "Strings": "Strings in python are surrounded by either single quotation marks, or double quotation marks.",
            "Booleans": "Booleans represent one of two values: True or False.",
            "type": " is used to verify the type of any object in Python",
            "Float": "is a number, positive or negative, containing one or more decimals.",
            "Comment": "Comments can be used to explain Python code.",
            "print": "print function is often used to output variables.",
            "elif ": "The elif keyword is Python's way of saying :if the previous conditions were not true, then try this condition.",}

#printing the dictionary items above
for word in glossary :
 print("\n" + word.title() + ": " + glossary[word])

