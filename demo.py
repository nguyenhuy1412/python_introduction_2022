# Function 
# print("Hello world")

# Arguments
# print("Something")

# Bug Syntax
# input("What is your name"

# Bug Logic
# a = input("a ")
# b= input("b ")
# print(a + b)

#Return value - Variable

# name = input("What is your name")
# print("Hello, "+name)

#Comment
"""
something will print out the result
"""

# name = input("What is your name?")
# print("STRIP ", name.strip())

# name = input("What is your name?")
# print("CAPITALIZE ", name.capitalize())

# name = input("What is your name?")
# print("TITLE ", name.title())

# name = input("What is your name?")
# print("SPLIT ", name.split())

# a = 3
# b=7
# print("a + b = ", a+b)
# print("a - b = ", a-b)
# print("a * b = ", a*b)
# print("a / b = ", a/b)
# print("a // b = ", a//b)
# print("a % b = ", a%b)
# print("a ** b = ", a**b)


# def PrintHello(name = "admin"):
# 	print("Hello, "+ name)

# def Sum(a, b):
# 	return int(a) + int(b)

# def GetName(fullName=""):
# 	firstName = fullName.split()[0]
# 	lastName = fullName.split()[1]
# 	return firstName, lastName

# IF

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#   print("x is less than y")
# if x > y:
#   print("x is greater than y")
# if x == y:
#   print("x is equal to y")

# ELSE IF 

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#   print("x is less than y")
# elif x > y:
#   print("x is greater than y")
# elif x == y:
#   print("x is equal to y")

# ELSE 

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#   print("x is less than y")
# elif x > y:
#   print("x is greater than y")
# else:
#   print("x is equal to y")

# OR 
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y or x > y:
#   print("x is not equal to y")
# else:
#   print("x equal to y")

# AND 
# score = int(input("Score: "))

# if score >= 90 and score <=100:
#   print("Grade A")
# elif score >= 80 and score < 90:
#   print("Grade B")
# elif score >= 70 and score < 80:
#   print("Grade C")
# elif score >= 60 and score < 70:
#   print("Grade D")
# else:
#   print("Grade F")

# MATCH 

# name = input("What's your name? ")

# match name:
#   case "Harry":
#     print("Gryffindor")
#   case "Hermione":
#     print("Gryffindor")
#   case "Ron":
#     print("Gryffindor")
#   case "Draco":
#     print("Slytherin")
#   case _:
#     print("Who?")

# a = 10
# b = [2,4,6,8]
# for i in range(a):
#   print(i)
# for i in range(len(b)):
#   print(i)


# students = {
#  "Harry": "Gryffindor",
#  "Hermione": "Gryffindor",
#  "Ron": "Gryffindor",
#  "Draco": "Slytherin"
# }
# for stu in students:
#  print(stu, students[stu], sep=", ")

# SyntaxError

# print("hello world )

# print(hello world")

# print("hello world"

# ValueError 

# try:
#   name = int(input("What is your name? "))
#   print(f"Good morning, {name}")
# except :
#   print("name must be an int")

# def get_int():
#   while True:
#     try:
#       x = int(input("What's x? "))
#     except ValueError:
#       print('x is not an integer')
#     else: return x

# def main():
#   x = get_int()
#   print(f"X value: {x}")

# main()

def register(backList, host):
  while True:
    try:
      x = int(input("What's id? "))
      if x == host:
        raise KeyError("id cannot match with host")
      if x in backList:
        raise KeyError("id in backlist. Poor for you")
    except ValueError:   
      pass
    else:
      print(f"{x} is successful register")
      break

register([222,333,444], 111)