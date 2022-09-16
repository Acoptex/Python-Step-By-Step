# Sets
# Exercise 1
# Open the names.csv file as .csv file and calculate the number of different names listed in that file
# Tips:
# The documentation for the csv module of Python can be found here: https://docs.python.org/3.6/library/csv.html.
# Use a set.
import csv

names = set()
with open('names.csv', newline='') as file:
    csv_file = csv.reader(file, delimiter=",")
  #  counter = 0
    for line in csv_file:
       # if counter != 0:
            names.add(line[1])
       # counter = counter + 1
print(len(names))
