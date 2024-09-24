#string cancatenation 
first_name="Vidhathri"
second_name="Gowda"
full_name=first_name+" "+second_name
print(full_name)

#repetition
message="warning! "*3
print(message)
#or
message1="Stop! "
print(message1 * 3)
#String Methods:
#upper(): Converts a string to uppercase.
#lower(): Converts a string to lowercase.
#strip(): Removes leading and trailing spaces from a string.
#replace(old, new): Replaces a substring with another string.

name=" Vidhathri Gowda "
print(name.upper())
print(name.casefold())
print(name.capitalize())
print(name.lower())
print(name.replace("Gowda","B J"))
print(name.strip())
print(name.count("v"))
print(name.endswith(" "))
print(name.find("a"))


statement='''Vidhathri said "Hello!"
Swathi said "hi!"'''
print(statement)
print(len(statement))#string length

#Accessing String Elements
print(name[3])
name2=name[3:]
print(name2.upper())