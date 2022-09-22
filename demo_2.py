# 
# from statistics import mean, median

# print(mean([10,20,25,30]))

# import sys
# if(sys.argv[1] == 'huy'): print("hello")
# if(sys.argv[1] == 'thong'): print("hello 2")
# print("hello, ", sys.argv[1])

# import sys
# from time import sleep
# try:
#   print("Start process")
#   print("Runing..")
#   sleep(5)
#   print("Done")
#   print("Hello", sys.argv[1],", your result is ready!")
# except IndexError:
#   print("Too few arguments" if len(sys.argv) < 2 else "Too many arguments")

# import cowsay
# import sys

# if len(sys.argv) == 2:
#   cowsay.cow("Hello, "+sys.argv[1])

import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(json.dumps(response.json(),indent=2))

import os
print(os.listdir())

with open("student.csv") as file:
  for line in file:
    row = line.rstrip().split(",")
    print(f"{row}")

with open("student.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    print(f"{name} is in {house}")


# SORT WITH KEY 

students = []
with open("student.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    student = {'name': name, 'house': house}
    students.append(student)

def get_name(student):
  return student["name"]

for student in sorted(students, key=get_name):
  print(f"{student['name']} is in {student['house']}")

# LAMDA FUNCTION 

students = []
with open("student.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    student = {'name': name, 'house': house}
    students.append(student)

for student in sorted(students, key=lambda x: x["name"]["something"]):
  print(f"{student['name']} is in {student['house']}")
  