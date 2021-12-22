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
