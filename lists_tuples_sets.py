
#-----------------------------------------------------------------------------------------------------------
#                                           VARIABLES...
#-----------------------------------------------------------------------------------------------------------

my_variable = "hello"
# list
grades = [77, 80, 90, 95, 100] # lists are ordered in the order we put elements in...

#tuple are immutable...cannot increase the size...cannot be mutated or changed......
tuple_grades = (77, 80, 90, 95, 100)

# set
set_grades = {77, 80, 90, 100} # unique and unordered...any duplicate data (hence un-unique, gets discarded...)

tuple_grades = tuple_grades + (100,) # this does not change the original tuple...this adds a new tuple to the existing tuple...

set_grades.add(60)

## Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

combo_set = your_lottery_numbers.intersection(winning_numbers)

combo2_set = your_lottery_numbers.union(winning_numbers) # this combines or unites both sets together into one unique unordered set...
# any duplicate numbers are not used...

diff = {1, 2, 3, 4}.difference({1, 2})

#print(your_lottery_numbers.intersection(winning_numbers)) # this produces another set with numbers that are in both the sets above...
#print(combo_set)
#print(combo2_set)

#print(diff)
#print({1, 2, 3, 4}.difference({1, 2})) # prints the difference between the sets...
#-----------------------------------------------------------------------------------------------------------
#                                           PRINT STATEMENTS...
#-----------------------------------------------------------------------------------------------------------

# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [50, 30, 20]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (10,) # don't forget the comma , otherwise Python will think you are doing a math operation due to using the ()...

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}
set2.add(9)
set2.add(12)
set2.add(77)
# could've just done this:
# set2 = {5, 77, 9, 12}

print(set1.intersection(set2)) # returns {5, 77, 9, 12}


mya_variable = "hello"

print(my_variable[0])
print(my_variable)

for char in my_variable: # iterables are strings, lists, sets, typles, etc...
    print(char)

for num in my_list:
    print(num)

    for numero in tuple_grades:
        print(numero ** 2)
        





#print(sum(grades) / len(grades))

#print(set_grades)

#grades.append(108)
#print(grades)

#print(tuple_grades)
