# strings are immutable

name = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
copy_name = name

print(name.upper()) # HAZZAZ
print(copy_name) # Hazzaz
print(name) # Hazzaz

print(name.lower()) # hazzaz

print(name.rstrip()) #remove right side white space and characters

print(name.lstrip("!")) #vice-verca of rstrip

print(name.replace("He", "Hazzaz")) # replace all the words to the expected words

print(name.replace("@", ""))

print(name.split(" "))

print(name.capitalize()) # make capital the first letter of ther sentence and make all the letters to lowercase

print(name.center(25))

print(name.count("Lorem")) # count number of occuerences
print(name.count("Lorem", 100, len(name)))


str1 = "Welcome to the Console"
print(str1.endswith("!!!")) # True
print(str1.endswith("e")) # True
print(str1.endswith("e", 0, len(str1) - 8)) # True



str1 = "He's name is Dan. He is an honest man."
print(str1.find("man")) # 34
print(str1.find("hazzaz")) # -1
print(str1.find("Dan", 10, len(str1))) # 13


str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan")) # 13
print(str1.index("hazzaz")) # sub string not found
print(str1.index("Dan", 0, 10)) # sub string not found
print(str1.index("Dan", 0, 20)) # 13



str1 = "WelcomeToTheConsole-------9999"
print(str1.isalnum()) # False
str1 = "WelcomeToTheConsole9999"
print(str1.isalnum()) # True


str1 = "Welcome"
print(str1.isalpha()) # True

str1 = "Welcom343434"
print(str1.isalpha()) # False


str1 = "hello world"
print(str1.islower()) # True

str1 = "Hello World"
print(str1.islower()) # False


str1 = "We wish you a Merry Christmas"
print(str1.isprintable()) # True

str1 = "We\tre wish you a Merry Christmas"
print(str1.isprintable()) # False


str1 = "Hello World  "  # False
print(str1.isspace())
str2 = "       "       
print(str2.isspace()) # True


# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str1 = "World Health Organization" 
print(str1.istitle()) # True

str1 = "hello world"
print(str1.istitle()) # False


# The isupper() method returns True if all the characters in the string are upper case, else it returns False.

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper()) # True

str1 = "WORLD health ORGANIZATION" 
print(str1.isupper()) # False


# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "hElLo" 
print(str1.swapcase())


# The title() method capitalizes each letter of the word within the string.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())