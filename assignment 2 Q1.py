# Assignment 2
# Question 1

given_string="Python is a case sensitive language"
#a.
print (f"length of the given string = {len(given_string)}\n")
#b.
print (f"the reversed string = {given_string[::-1]}\n")
#c.
x=slice(given_string.index('a'),given_string.index('l')-1)
new_string=given_string[x]
print (f"new string using slice = {new_string}\n")
#d.
new_string=new_string.replace ("a case sensitive","object oriented")
print (f"{new_string}\n" )
#e.
print (f" index of a = {given_string.index('a')}\n")
#f.
given_string=given_string.replace(' ','')
print (f"given string after removing")