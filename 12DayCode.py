# String Methods
# Strings are immutable 
a = "Harry"
print(len(a))
# uppercase :-The upper() method converts a string to upper case.
print(a.upper())

#lowercase() :-The lower() method converts a string to lower case.
print(a.lower())
 
# strip():-The strip() method removes any white spaces before and after the string.
str2 = "  AmitojSingh  "
print(str2.strip())

#rstrip() :- the rstrip() removes any trailing characters. Example:
str3 = " Amitoj!!!!!"
print(str3.rstrip("!"))

# 2nd Example
str4 = "  AmitojSingh!!!!!!! "
# print(str4.strip())
# print(str4)

# replace() : -The replace() method replaces all occurences of a string with another string.
str5 = "Harry"
print(str5.replace("Harry" , "John" ))

#split() : - The split() method splits the given string at the specified instance and returns
#  the separated strings as list items.
str6 = "Silver Spoon"
print(str6.split(" ")) 

# capitalize() :- The capitalize() method turns only the first character of the string to uppercase and the rest 
# other characters of the string are turned to lowercase. The string has no effect if the 
# first character is already uppercase.
str7 = "introduction of Python"
print(str7.capitalize())

# center() :-The center() method aligns the string to the center as per the parameters 
# given by the user.
str8 = "AmitojSIngh"
print(len(str8),str8.center(50))

# count() :
# The count() method returns the number of times the given value has 
# occurred within the given string.
str9 = "Abracadabra"
countStr = str9.count("a")
print(countStr)

#endswith():- The endswith() method checks if the string ends with a given value. 
# If yes then return True, else return False.

# This String return True value 
str10 = "Amitoj Singh"
Strend = str10.endswith("Singh")
print(Strend)

# This String return False value 
str11 = " Amitoj Singh"
Strend = str11.endswith("!!!!")
print(Strend)

#find() :- The find() method searches for the first occurrence of the given value and returns the index where it is present. 
# If given value is absent from the string then return -1.
str12 = "My name is Amitoj Singh"
print(str12.find("is"))
print(str12.find("ishh"))
# print(str12.index("ishhh"))

# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
# If any other characters or punctuations are present, then it returns False.
str13 = "godgifited"
print(str13.isalnum())
# 2nd example 
str14 = "Welcome to vscode"
print(str14.isalnum())

# isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. 
# If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str15 = "Welcometovscode20"
print(str15.isalpha())
# 2nd Example 
str16 = "AmitojSingh"
print(str16.isalpha())

#lowercase :
# The islower() method returns True if all the characters in the string are lower case, 
# else it returns False.

# return for true 
str17 = "amitojsingh"
print(str17.islower())

#return for false
str18 = "AmitojSingh"
print(str18.islower())

# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, 
# if not, then return False.

str19 = "AmitojSingh"
print(str19.isprintable())

# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

str20= "       "       #using Spacebar
print(str20.isspace())
str21 = "        "       #using Tab
print(str21.isspace())
