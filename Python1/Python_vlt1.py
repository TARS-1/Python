#Integers and Floats
int1 = 35
float1 = 35.556

#Strings
str1 = "Hello World"
str2 = "35"

#Booleans
bool1 = True
bool2 = False

#Prints
print ("Hello World")

#Print with string variables
str1 = "Adam"
print ("Hello " + str1)

#Print with integer variables
int1 = 78
print ("The number is " + str(int1)) #convert int to str for the text
float1 = 78.8
print ("The number is " + str(float1))#same as above

#Print with booleans
bool1 = True
print ("Person is above 20  years old: " + str(bool1)) #same as above, but with bools

#String functions
str1 = "Hello World"
str1.lower() #makes every letter lowercase
str1.upper() #every letter uppercase
str1.isupper() #returns a bool val if the string is uppercase
str1.islower() #same as isupper but for lowercase
len(str1) # returns the number length of the string
str1[0] #returns the letter at the specified index
str1.replace("Hello", "Goodbye") #replaces the first word with the second word
print("Hello Everyone")