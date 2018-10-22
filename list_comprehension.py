
"""
PROGRAMMATICALLY CREATING A LIST: an_equal_list = [x for x in range(5)]
HENCE, List Comprehension
"""

my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)] # [0, 1, 2, 3, 4]
print(an_equal_list)
print(" ")
print(an_equal_list[0])
print(" ")



multiply_list = [x * 3 for x in range(5)]
print(multiply_list)
print(" ")
print(multiply_list[2])


print("Modolus Result " + str(8 % 3))

print("Odd or Even ? " + str(9 % 2))
print(" ")


print([n for n in range(10) if n % 2 == 0])

even_nums = [n for n in range(10) if n % 2 == 0]

print(even_nums)

people_you_know = ["Rolf", " John", "anna", "GREG"]
# strip the white spaces and make all strings lowercase...
normalized_people = [person.strip().lower() for person in people_you_know]
print(" ")
print(" ")
print(normalized_people)
