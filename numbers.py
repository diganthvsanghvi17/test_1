# this is a python project to learn python from scratch with version control
# this exercise is checking version control and coding in python

#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

#create the variables
length = 92
breath = 48.8
# write the formula for area
area = length * breath
# print the output
print(area)

# You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?

#declaring variables

num_packets = 9
cost_chips = 1.49
money_given = 20

# calculating the total spend amount

total_spend_amount = num_packets * cost_chips
money_returned = money_given - total_spend_amount

# print the output
print('$'+str(money_returned))

#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet,
# how much will be the total cost to replace all tiles. Calculate and print the cost using python

#declaring variables

length_bathroom = 5.5
cost_tiles = 500

# logic implementation:
area_bathroom = length_bathroom**2
total_cost = area_bathroom*cost_tiles

# printing the output

print("RS" + " "+str(total_cost))

# Print binary representation of number 17
#declaring variable
number=17
# logic implementation
binary = f'{number:08b}'
#printing of output
print(binary)