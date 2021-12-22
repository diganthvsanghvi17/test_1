# new string exercise file
# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
# declaring the variables
street = "seaseme street"
city = "new york"
country = "USA"
# implementing the logic

address_1 = street + "\n" + city + "\n" + country
address_2 = f'{street}\n{city}\n{country}'

# printing the address
print("the address using the operator: \n",address_1)
print("the address according to fstring:\n",address_2)

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index

#declaring the variables
given_string = "Earth revolves around the sun"
# printing the output
print(given_string[6:14])
print(given_string[-3:])

