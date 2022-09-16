some_list = ['a', 'b', 'c', 'd', 'd', 'e', 'c']

# duplicates = []
#
# for char in some_list:
#     if some_list.count(char) > 1:
#         if char not in duplicates:
#             duplicates.append(char)


duplicates = [char for char in some_list if some_list.count(char) > 1 and if char !=char]
print(duplicates)