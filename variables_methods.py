# https://www.udemy.com/automated-software-testing-with-python/learn/v4/t/lecture/7736868?start=0

a= 5
b = 10
my_variable = 56
my_10_variable = 10

string_variable = "hello"
single_quotes = 'strings can have single quotes...'


print(my_variable)
print(single_quotes)


#===============================================================================
# --------------------------------------------------------------
#                    **FUNCTION DEFINITIONS**
# --------------------------------------------------------------
def my_print(my_param):
    #result = str(my_param)
    #global my_param
    print(my_param)
    #print("World")


def my_multiply_method(num_one, num_two):
    result = num_one * num_two
    print( "The answer is: " + str(result))


def my_multiply_method_2(num_one, num_two):
    return num_one * num_two

    #return "The answer is: " + str(result)
    #print( "The answer is: " + str(result))


# --------------------------------------------------------------
#                ** FUNCTION DEFINITIONS END **
# --------------------------------------------------------------

#                       FUNCTION CALLS...
#-------------------------------------------------------------------------------

#my_print("Suzanne")

#my_print(str(9873495873))

#my_multiply_method(5, 7)

#result = my_multiply_method_2(45, 45)

#print(result)
#print("This is the output from function: my_multiply_method_2 " + str(result))



# pass function as argument to another function...
my_print(my_multiply_method_2(5, 3))
