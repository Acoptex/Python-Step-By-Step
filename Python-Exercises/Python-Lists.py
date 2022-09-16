some_list = ['a', 'b', 'c', 'd', 'd', 'e', 'c']

duplicates = []

for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)
print(duplicates)
