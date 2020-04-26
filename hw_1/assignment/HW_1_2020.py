#Exercise 1: Operators (1 point)

#Assign the output of all operations to the corresponding variables and print their values.
#See 'Operators and Expressions' chapter in 'A Byte of Python'
# (a): 2 plus 3
# (b): append string '9' to variable a. Use an appropriate function to convert a to string. Ouput: '59'
# (c): append strings 'Hello', space and 'World!'. OUTPUT: 'Hello World!'
# (d): add 3.5 to 10 and multiply the sum by 2 
# (e): 3 to the power of 3
# (f): d is equal to e. Output: True
# (g): modulo of 6 divided by 3

#Answer:
print('Exercise 1')
a = 2 + 3
print(a)

#finish by yourself


#Exercise 2: Lists (1 point)

#See 'Data Structures - List, Sequence' in 'A Byte of Python'
#Use list index operator operator [] and list slicing to complete the task.
# (a) append two lists as list3 and print the result.
list1, list2 = [1, 2], [3, 4]
# (b) assign the first element in the list grades to the variable first and print it. Use [] operator.
grades = ['1.0', '2.3', '1.3', '2.3', '3.0', '1.3']
# (c) update the third grade ('1.3') in the list to the value 'F' and print the updated list
#Slicing for the updated list:
# (d) assign all grades except the first and last to the list middle and print it (use one statement for that)
# (e) assign last three grades to the last_three list and print the result (using one statement)

#Answer:
print('\nExercise 2')
list3 = list1 + list2
print(list3)
#finish by yourself


#Exercise 3: List methods (1 point)

#Your are given an animal list. Make all transformations with it.
animals = ['cow', 'dog', 'fox', 'horse', 'penguin']
# (a) use .append() method to add 'zebra' to the list
# (b) use .insert() method to insert 'eagle' in the position of the horse, find its position with index(). Horse should stay in the list
# (c) store the length of the final list in the variable animals_list_length. Use len() function for that.

#Answer:
print('\nExercise 3')
animals.append('zebra')
#finish by yourself


#Exercise 4: Financial Calculator (3 points)

# Write the following program:
# - the user is asked to enter a principal amount (EUR), an interest rate (%) and a term of the loan (years)
# - the user is asked to specify the type of the interest: simple or compound
# - the program computes the interest based on user input, stores the result in interest variable and prints it out.
# Input check is not necessary, assume that the user enters floats, ints or strings where necessary.
# TIP: use formulas from Investopedia https://bre.is/6SwFW9Cx

#Sample input/output:
"""
Welcome, user. I am a financial calculator.
Enter principal amount (EUR): 5000
Enter annual interest rate (%): 7.2
Enter period (years): 2
Should I calculate compound interest (y/n): y
745.92
"""

#Answer:
print('\nExercise 4')
# get user input
principal = input("Welcome, user. I am a financial calculator.\nEnter principal amount (EUR): ")
#finish by yourself


#Files to submit
# when you are done, name this file as solution_hw.py and upload to Moodle