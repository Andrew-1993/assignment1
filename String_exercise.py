""" String Exercise"""

""" Task 1 - Write a program to create a new string made of the middle three characters of an input string.
"""
input = "JhonDipPeta"
print(input[4:7])

#result = Dip



""" Task 2 - Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""

s1 = 'Aunt'
s2 = 'Sister'
s3 = s2[:len(s2)//2] + s1 + s2[len(s2)//2:]
print(s3)
#s3 = SisAuntter

""" Task 3 Given two strings, s1 and s2, write a program 
to return a new string made of s1 and s2’s first, middle, and last characters."""

s1 = 'America'
s2 = 'Japan'
s3 = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]
print(s3)
#s3 = AJrpan

""" Task 4
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced
 if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
"""

s1 = "Yn"
s2 = "PYnative"
s3 = s1 in s2
print(s3)
#result = True

s1 = "Ynf"
s2 = "PYnative"
s3 = s1 in s2
print(s3)
#result = False

""" Task 5 - Write a program to split a given string on hyphens and display first and last substring."""

str1 = 'Emma-is-a-data-scientist'
x = str1.split("-")
print(x[0] + ', ' + x[-1])

#result = Emma, scientist


""" Task 6
Reverse a given string
Write a program to find the last position of a substring “Emma” in a given string.
"""

str1 = "Emma is a data scientist who knows Python. Emma works at google."
x = str1[::-1]
print(x)
index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)
#Result = Last occurrence of Emma starts at index 43
