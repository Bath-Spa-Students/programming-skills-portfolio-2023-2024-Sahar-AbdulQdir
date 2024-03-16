#inserting a dictionary
glossary = {"Integer": "is a whole number, positive or negative, without decimals, of unlimited length.",
            "List": "are used to store multiple items in a single variable.",
            "sys": "is used to check the Python version of the editor",
            "Strings": "Strings in python are surrounded by either single quotation marks, or double quotation marks.",
            "Booleans": "Booleans represent one of two values: True or False."}

#printing the dictionary items above
word = "Integer"
print("\n" + word.title() + ": " + glossary[word])

word = "List"
print("\n" + word.title() + ": " + glossary[word])

word = "sys"
print("\n" + word.title() + ": " + glossary[word])

word = "Strings"
print("\n" + word.title() + ": " + glossary[word])

word = "Booleans"
print("\n" + word.title() + ": " + glossary[word])