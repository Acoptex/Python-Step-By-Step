# Root and square
my_list = [5, 4, 3]
new_list = list(map(lambda item: item * (1 / 2), my_list))
print(new_list)  # Result should be: [2.5, 2.0, 1.5]
new_list = list(map(lambda item: item ** 2, my_list))
print(new_list)  # Result should be: [25, 16, 9]

# List sorting
# Sort the tuples by second key number
# Result should be: [(10, -1), (0, 2), (4, 3), (9, 9)]
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda item: item[1])
print(a)
