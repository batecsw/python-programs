# Write your code here :-)

# Code challenge 1
name = "Amelie"
age = 10
year_of_birth = 2013
print("This is", name, "they are",  age, "years old and were born in", year_of_birth)

# Code challenge 2
name = input("please type in your name: ")
country = input("please type in which country you were born in: ")
date_of_birth = input("please type in your date of birth: ")
print("This is", name, "they were born in",  country, "and were born on", date_of_birth)

# Code challenge 3
for i in range(1, 11):
    print(i, "x 2 =", i*2)

# Code challenge 3 bonus
students = ["Amelie" , "Tam Anh", "Max", "Mose", "Michael", "Roberto"]
for student in students:
    print(student)

# Code challenge 4
# Note that Python by default treats all inputs as strings. If we want to treat it
# as a different data type we must cast it, in this case to an integer using int
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 140 and age >= 11:
    print("You are allowed on all the rides")
elif height >= 110:
    print("You are only allowed on the junior rides")
else:
    print("You are not allowed on any rides")

# Code challenge 5
from random import randint
for i in range(5):
    print(randint(1, 100))

# Code challenge 6
def square(num):
    return num*num

user_number=int(input("Enter a whole number: "))
print("The square of", user_number, "is", square(user_number))

