# Variables and Data Types

character_Name = "John"  # using string to store the value of the character name
character_Age = "35"  # using numbers to store the value of the character age
character_Age2 = 35.67  # can use decimals too
character_Bool = True  # using booleans for true and false

print("There once was a man named " + character_Name + ", ")
print("he was " + character_Age + " years old.")

character_Name = "Mike Hawk"  # updating the value in character name to mike hawk xD
print("He really liked the name " + character_Name + "\nbut didn't like being " + character_Age + ".")

# String Practice

print("Hello\"World")  # allows you to print a quotation mark

sent = "Hello World 2"

print(sent.lower())  # lower() changes the string to all lower case letters
print(sent.upper())  # you get the idea

print(sent.isupper())  # checks to see if the string is uppercase. Returns true if uppercase, false otherwise

print(sent.upper().isupper())  # makes the string uppercase, then checks to see if it is uppercase

print(len(sent))  # finds the length of the string. The number of characters in the string
print(sent[0])  # gets one of the characters that is specified inside the []
print(sent.index("H"))  # returns the index of the H in our string
print(sent.replace("Hello", "Goodbye"))  # replace words. The first quotes is the area you want to be replaced and the second quotes is what you want to replace it with

# Number Practice

my_num = 5
print(my_num)
print(10 % 3)

print(str(my_num) + "is my favorite number")  # convert a number to a string

testNumb = -5
print(abs(testNumb))  # find the absolute val of the number
print(pow(testNumb, 2))  # the first is the number and the second is the power that it is being raised to
print(max(4, 6))  # returns the larger of the two numbers
print(min(4, 6))
print(round(3.2))  # rounds the number

# importing
from math import *

print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

# input from user
userName = input("Enter your name: ")
userAge = input("Enter your age: ")

print("Hello " + userName + "!\n")
print(userName + ", you are " + userAge + " years old")

# calculator

userNum = input("Enter a number: ")
userNum2 = input("Enter a second number: ")

result = float(userNum) + float(userNum2)
print(result)

# Mad Libs Game

color = input("Enter a color: \n")
plurNoun = input("Enter a plural noun: \n")
celeb = input("Enter a celebrity name: \n")

print("Roses are " + color)
print(plurNoun + " are blue")
print("I love " + celeb)

# Lists


list1 = ["Suck", "It", "Oscar"]  # you can enter string, numbers, and bools

listAccess = list1[1]  # accessing a specific index of the list
listAccess2 = list1[0]  # can also do print (list1[0])
listAccessBack = list1[-1]  # can also do list1[-1 or -2 or -3 to access the list backwards
listAccessMult = list1[1:]  # returns the element at the index and everything after that
listAccessRange = list[1:3]  # returns element at index and everything up to the last index except for the last index
list1[1] = "Deez Nuts"  # replaces the specified element

print(listAccess)
print(listAccess2)

# list Functions

lucky_numbers = [4, 2, 3, 5, 7, 5, 8]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# extend function: allow you to take a list and append another list to the end of it
friends.extend(lucky_numbers)

# append function: allows you to append another item to the list
friends.append("Michael")

# insert function: insert an item into a list. 2 params, 1st is the index where you want to insert the item
# 2nd param is the thing you want to enter
friends.insert(1, "Kelly")

# remove is the same thing as insert, just removing the selected element
friends.remove("Jim")

# remove the entire list
friends.clear()

# pop function: pops the last element off of the list
# friends.pop()

# prints the index of the specified element
# print(friends.index("Kevin"))

# count counts the number of times a specific element is in the list
# print (friends.count("Jim"))

# sorts the list in alphabetical order
friends.sort()

# reverse the elements of the list
lucky_numbers.reverse()

# copy function
friends2 = friends.copy()

# Tuples
# Data structrue that stores values

coordinates = (4, 5)
print(coordinates[0])  # print a value inside a tuple based on their index


# Functions
# declaring the function
def greet_user(user_name):
    name = input("What is your name:")
    print("Hello " + name + "! There is another person here called" + user_name)


# calling the function
greet_user("Kcey")


# Return Statements
def cube(num):
    return num * num * num


output = cube(4)
print(output)

# If statements
is_male = True
is_tall = True

if is_male or is_tall:
    print("The person is a male or is tall")
elif is_male and is_tall:
    print("you're good homie")
elif is_male and not (is_tall):
    print("WTF")
else:
    print("The person is a legal nugget(basically meaning that they short af)")

    # Comparisons


def max_numb(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3


output = max_numb(3, 4, 5)
print(output)

# Dictionaries

monthConversions = {
    "Jan": "January",  # You can use numbers instead of jan, feb
    "Feb": "February",
    "Mar": "March",

}

print(monthConversions["Feb"])
print(monthConversions.get("Luv", "Not a valid key"))

# While loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

# for loops
friends = ["jim", "karen", "kevin"]
for friend in friends:
    print(friend)

for friend1 in range(len(friends)):
    print(friends[friend1])

# loop throudh numbers
for index in range(10):
    print(index)

for index1 in range(3, 10):
    print(index1)

for index2 in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first iteration")

        # Exponent function
print(2 ** 3)  # 2^3


def exponent_func(base_num, pow_num):
    result = 1
    for index_num in range(pow_num):
        result = result * base_num
    return result


print(exponent_func(3, 2))

# 2d list and nested loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[1][0])  # index is the number of the row, so 0,1,2,3
# first [] is the row and the second [] is the column

for row in number_grid:
    for col in row:
        print(col)

# large comments
'''
hello everyone

'''

# Try except
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero")  # or print (err)
except ValueError:
    print("Invalid input")
except:
    print("every error")

    # Reading files
employee_file = open("employees.txt","r")  # file name. R is to read the file, W is to change the file infor (write to the file), A is to add new info to the file, R+ read and write
print(employee_file.readable())  # tells whether or not we can read the file
print(employee_file.read())
print(employee_file.readline())
print(employee_file.readlines())
print(employee_file.readlines()[1])

for employees in employee_file.readlines():
    print(employees)

employee_file.close()  # closes the file

# Writing to files
employee_file = open("employees.txt", "a")
employee_file.write("Toby - H.R.")
employee_file.write("\n Kelly - Customer Service")

employee_file = open("employees.txt", "w")
employee_file.write("\n Kelly - Customer Service")

employee_file = open("employees1.txt", "w")  # creates another file
employee_file.write("\n Kelly - Customer Service")

# Modules and Pip
import tools

print(tools.roll_dice(10))

# classes and objects

from studentClass import Student

student1 = Student ("Kcey", "Computer Science", 3.1, False)

print (student1.name)