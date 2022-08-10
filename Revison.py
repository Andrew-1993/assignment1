# Revision for Numeric, String and Sequence Data Types

""" Task 1
read function range()
https://docs.python.org/3/library/stdtypes.html#range

Reverse the order of words in a given sentence.
"""

str_val = "Hello World"
words = str_val.split()
words = list(reversed(words))
print(" ".join(words))

#output = "World Hello"

""" Task 2
Write a program  that takes a list and returns a new list that contains all the elements of 
the first list minus all the duplicates.
hint: use set() =>
"""

list1 = [10, 23, 23, 5, 67, 10]
list2 = list(set(list1))
print(list2)

#output = [10, 23, 5, 67]

""" Task - 3
Write a password strength verifier in Python that checks if user password is strong.
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
"""

pas = 'food'

import string
a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
f = [a,b,c,d]
sum1 = 0
for x in f:
    sum1 +=(set(pas) & set(x)) != set()
print('True' if sum1==4 else 'False')

#result = False

password = '1EggPerD@y'
import string
a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
f = [a,b,c,d]
sum1 = 0
for x in f:
    sum1 +=(set(password) & set(x)) != set()
print('True' if sum1==4 else 'False')


#result = True

""" Task 4- Write a program to reverse row sort in list of lists
"""

list_id = [[4,1,6], [7,9], [8,9,2,4]]
for ele in list_id:
    ele.sort(reverse=True)
print("The reverse sorted list is : " + str(list_id))

#result = [[6,4,1], [9,7], [9,8,4,2]]


""" Task 5 
Write a program to pair elements with rear element in matrix row
"""

list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
res = []
for x in list1:
    res.append([[ele, x[-1]] for ele in x[:-1]])
print(res)

#result = [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]

""" Task 6
Replace each special symbol with # in the following string
Hint: import string, and use string.punctuation
"""

str1 = "%There &are three( students$ and& 1 trainer!"
import string

str2 = ""
for i in str1:
    if i in string.punctuation:
        str2 +='#'
    else:
        str2 += i
print(str2)

#result = "#There #are three# students# and# 1 trainer#"


""" Task 7
Remove all characters for string except integers
hint: list comprehension and isdigit()
"""

str1 = "My mum has a 10 year old dog and 2 fishes"
print(''.join(i for i in str1 if i.isdigit()))


#result = 102

""" Task - 8
Remove all empty strings from a list of strings
hint: use filter() => https://docs.python.org/3/library/functions.html#filter
"""

name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']

name_list = list(filter(None, name_list))
print(name_list)

