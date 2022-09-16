# PriorityQueue
# Exercise 1
# Find out the 5th most common first name assigned in the USA.
# Tip:
# Read the names.csv file. First use a dictionary with which you count
# the frequency of first names and then a priority queue to determine
# the top 5 first names.

import csv
import queue

names = {}
with open('names.csv', newline='') as csvfile:
    namereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    counter = 0
    for line in namereader:
        if counter != 0:
            number = int(line[5])
            name = line[1]

            if name in names:
                names[name] = names[name] + number
            else:
                names[name] = number
        counter = counter + 1

pq = queue.PriorityQueue()

for name, number in names.items():
    pq.put((-number, name))
counter=0
for i in range(0, 50):
    print(pq.get())
    if counter ==4:
        print("Value is "+ str(pq.get()))
    counter +=1
