# should_continue = True
# if should_continue:
#     print("Hello")

# Ctrl / for commenting out a block of code...
#known_people = ["John", "Anna", "Mary", "Sue"]
#person = input("Enter the person you know: ")


# if person in known_people:
#     print("You know this person " + person + "!")
# else:
#     print("You don't know anyone in our club. You should join.")


# if person in known_people:
#     #if person.islower() || person.isupper()
#     print("You know this person " + person + "!")
#
# if person not in known_people:
#     print("You don't know anyone in our club. You should join.")


# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     #print("You don't know {}!".format(person))
#     print("You don't know anyone in our club. You should join.")
#


#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
# def even_numbers():
#     evens = []
#     for number in numbers:
#         if number % 2 == 0:
#             evens.append(number)
#             print(evens)
#     return evens
#     print(evens)
#
# print(numbers)
#
# even_numbers()
#
# even_number_output = even_numbers()
# print(" ")
# print(even_number_output)


#
# def user_menu():
#     if choice == "a":
#         return "Add"
#     elif choice == "q":
#         return "Quit"


#---------------------------MY SOLUTION-----------------------------------------

# def who_do_you_know():
#     # Ask the user for a list of people they know
#     user_list = []
#     user_input = input("Please enter a list of people you know separate by commas... ")
#     # Split the string into a list
#     user_list = user_input.split(',')
#     # Return that list
#     return user_list
#
# output = who_do_you_know()
#
# name_data = output
# print(" ")
# #print(result)
# print(output)
#
#
# def ask_user():
#     global name_data
#     # Ask user for their name
#     person_user_knows = input("Please type person you know: ")
#     # See if their name is in the list of people they know
#     if person_user_knows in name_data:
#         # Print out that they know the person
#         print("You know this person!")
#     else:
#         print("This person is not on the list. ")
#
#
# ask_user()

#---------------------------MY SOLUTION END--------------------------------------


#---------------------------INSTRUCTOR SOLUTION----------------------------------

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",")
    #people_without_spaces = []
    people_without_spaces = [person.strip() for person in people_list]
    #people_without_spaces = [person.strip().lower() for person in people_list]
#    for person in people_list:
#       people_without_spaces.append(person.strip())

    return people_without_spaces
    #return people_list




def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You know no one on our list. ")

ask_user()



#---------------------------INSTRUCTOR SOLUTION END-------------------------------
