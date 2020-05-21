#datatypes
#1. Int --> 4 7 -5 34 100
#2. Float --> 3.7 4.2 33.9  47.856
#3. Boolean --> True False
4 > 7

#hello
"""
hello
"""

"""
#mathematical operators
+
-
3/2 --> 1.5
3//2 --> 1
2**5 --> 32
8 % 2 --> 0
7 % 2 --> 1

#comparison operators
4 > 7 --> False
13 < 20 --> True
7 == 3 + 4 --> True
7 >= 8  --> False
7 <= 8 -- True 
20 != 25 --> True

#Order of operations and parenthesis - BEDMAS 
# () --> grouping
# ** --> exponents
# +x -x --> positive, negative
# * / % // -->  mult, divide, remainder, quotient
# +- --> addition, subtraction

"""

#BEDMAS 
print(2 + 3 - 4)

#strings
print("this is a string")
print("hello " + "my name is afnan")
print("hello" * 2)

"""
print("hello" * 3.0)
#this will not work bc it is an integer
"""

print("a" > "c")
#bc of the ASCII table search on google, capital comes for small letters. eg.capital is 65 and then goes higher and small is 97 and goes higher

print("Y" > "f")
print(ord("Y")) #will tell you the position on ASCII chart 
print(ord("f"))
print("F" == "f")  

print("hello" , "my name is afnan")
#the comma adds a space

"""
print("your number is:" + 7) 
#can't connect string and integer only string and string
"""

print("first line")
print("second line")

print("first line" , end= " ")
print("second line")

#  /n -- says new line
# end= what you want to happen at end of a print statement

#TYPE CONVERSION
#str --> int
#int --> str
#str --> float

print("your number is:" + str(7))
print("your number is:" + str(4/2))
print("your number is:" + str(3.4))
print("your number is:" + str(True))

#variable - will always be there and can be used anytime, think of it like a box that contains something

#VARIABLES
number = 7
print("number firstly is" , number)
number = 7 * 3 
print("number secondly is" , number)
print("lets print number again" , number)
number = 4 < 7

#variable can be anything, no spaces, only underscores

val = 7
firstnum = 43
myage = 35
babysfirstwords = "mama"
babys_first_words = "mama"

X = "47"

print(val)

myage = 7
myageplusseven = int(myage) + 7
print("my age after seven years is " + str(myageplusseven))

userinput = input("Enter your input: ")
print(userinput)
print("your number is " + userinput) 

mystring = "47"
print(float(mystring))
print(int(mystring))
myint = 37

print(str(myint))
myfloat = 4.8
print(str(myfloat))
print(int(myfloat))

"""
userinput = input ("Enter your input: ")
print(int(userinput) + 5)
print("your number is " 





