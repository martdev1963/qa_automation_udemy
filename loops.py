my_list = [1, 2, 3, 4, 5, 6, 7]

for num in my_list:
    print(num ** 2)

print(" ")
tuple_grades = (23, 78, 89, 90, 65, 45)

for numero in tuple_grades:
    print(numero)


user_wants_number = True
#try:
#    while user_wants_number == True:
#        print(10)
#except KeyboardInterrupt:
#    pass

print(" ")
user_name = input("Hello, I'm Adele, what is you're name? ")
while user_wants_number == True:
    print(10)
    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False
        print("Thank you " + user_name + " for your interaction! See you later.")
