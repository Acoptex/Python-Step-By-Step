# Create a function my_func which will have as a parameter list 'my_list' of integers
# which will print the highest even number
def my_func(my_list):
    # highest_number = 0
    # for item in my_list:
    #     if item % 2 == 0 and item > highest_number:
    #        highest_number = item
    # return highest_number

    evens = []
    for item in my_list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(my_func([1,2,3,4,5,6]))