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

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.

#declaring the variables:

num_of_vegetabels = 3
num_of_fruits = 4

# printing te output

print(f"I eat {num_of_vegetabels} veggies and {num_of_fruits} fruits daily")
print("I eat" +" " +str(num_of_vegetabels) +" "+ "veggies and " + str(num_of_fruits) + " fruits daily")
