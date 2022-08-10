# List Exercise

""" Task 1- Reverse a given list in python"""

info = ['karl', '100', 'Red', 'Mangoes']
info.reverse()
print(info)

""" Task 2 - Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Hint: use list comprehension with zip function"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [x + y for x, y in zip(list1, list2)]
print(list3)
print(' '.join(list3))
#result = ['My', 'name', 'is', 'Kelly']

'''
Task 3 - Write a Python program to find the second largest number in the given list.
'''
list1 = [10, 20, 4]
list1.sort()
print(list1[-2])

#result: 10

list2 = [70, 11, 20, 4, 100]
list2.sort()
print(list2[-2])
#result: 70

""" Task 4 - Concatenate two list
Hint: use list comprehension <<new_list>> = [expression for item in list1 for y in list2]"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
new_list = [x + y for x in list1 for y in list2]
print(new_list)

#result = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

""" Task 5 -Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item."""

list1 = [5, 10, 15, 20, 25, 50, 20]
output = [200 if x==20 else x for x in list1]
print(output)

#result = [5, 10, 15, 200, 25, 50, 200]

""" Task 6 -count number of occurrences of x in the given list"""
list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(list.count(x))
#result : 3  #10 appears three times in given list.

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 16
print(lst.count(x))
#result : 0

""" Task 7 - write a program to remove all occurrences of item 20
Hint: list comprehension"""

list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = [x for x in list1 if x!=20]
print(list2)

""" Task 8 - Write a program to return the middle value of a list. If there are 2 middle values, return the second
"""

names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
middle_name = names[len(names)//2]
print(middle_name)
#result = 'pineapple'

age = [10, 3, 45, 67, 89.0, 45]
middle_numb = age[len(age)//2]
print(middle_numb)
#result = 67

