#Exercise 1: Operators (1 point)

#Assign the output of all operations to the corresponding variables and print their values.
#See 'Operators and Expressions' chapter in 'A Byte of Python'
# (a): 2 plus 3
# (b): 2.0 plus 3.0
# (c): string '2' append to '3'. OUTPUT: '23'
# (d): 2 multiply by 3
# (e): 2 to the power of 3
# (f): 5 divided by 3 and rounded down
# (g): modulo of 5 divided by 3

#Answer:
print('Exercise 1')
a = 2 + 3
print(a)

b = 2.0 + 3.0
print(b)

#finish by yourself (c)-(g)
c = '2' + '3'
print(c)

d = 2 * 3
print(d)

e = 2 ** 3
print(e)

f = 5 // 3
print(f)

g = 5 % 3
print(g)


#Exercise 2: Type conversion (1 point)

#Python provides the built-in functions: int(), float(), str() to convert variables to another type,
#e.g., str(3) converts integer 3 to the string '3'.
# Calculate the mathematical sum of numbers stored in var1, var2, and var3 and assign to my_sum variable
# Make the calculation in one line and use type-conversion functions to transform var1 and var2 to numbers.
var1 = '2'
var2 = '3.0'
var3 = 5

#Answer:
print('\nExercise 2')
#finish by yourself
my_sum = int(var1) + float(var2) + var3
print(my_sum)


#Exercise 3: Lists (1 point)

#See 'Data Structures - List, Sequence' in 'A Byte of Python'
#Use list index operator operator [] and list slicing to complete the next task.
# (a) append two lists as list3 and print the result.
list1, list2 = [1, 2], [3, 4]
# (b) assigne the second grade to the variable second and print it
grades = ['1.0', '2.3', '1.3', '2.3', '3.0', '1.3']
# (c) update the second grade ('2.3') in the list to the value '1.3' and print the updated list
#Slicing for the updated list:
# (d) assign first two grades to the list first_two and print it (use one statement for that)
# (e) assign all grades except the last one to the list except_last and print the result (using one statement)
# (f) assign last two grades to last_two list and print the result (using one stetement)

#Answer:
print('\nExercise 3')
list3 = list1 + list2
print(list3)
#finish by yourself
second = grades[1]
print(second)
grades[1] = '1.3'
print(grades)
first_two = grades[0:2]
print(first_two)
except_last = grades[:-1]
last_two = grades[-2:]
print(last_two)


#Exercise 4: List methods (1 point)

#Your are given a list. Make all transformations with the same list.
animals = ['cow', 'dog', 'fox', 'horse', 'penguin']
# (a) use .append() method to add 'zebra' to the list
# (b) use .insert() method to insert 'elephant' in the second position of the list
# (c) use del to delete the last element from the list. Print the final result

#Answer:
print('\nExercise 4')
animals.append('zebra')
#finish by yourself
animals.insert(1, 'elephant')     #insert a string with the index 1 (second element). Other element are shifted
del animals[-1]                   #remove the last (first from the end)
print(animals)

#Exercise 5: The Very Basic Calculator (2 points)

# Write the following program:
# - the user is asked to enter the first number
# - the user is asked to enter the second number
# - the user is asked to enter an operator: "+", "-", "*", or "/"
# - the calculator computes the answer for entered two numbers, stores the result in calculation_result variable and prints it out.
# If user enters an invalid operator, the programs prints nothing.

#Sample input/output:
"""
Welcome, user. I am a very basic calculator.
Enter the first number: 2
Enter the second number: 6
Enter operator (+, -, *, or /): -
-4.0
"""

#Answer:
print('\nExercise 5')
# get user input
first_number = input("Welcome, user. I am a very basic calculator.\nEnter the first number: ")
#finish by yourself
second_number = input("Enter the second number: ")
# transform the input to float
first_number = float(first_number)
second_number = float(second_number)
operator = input("Enter operator (+, -, *, or /): ")
# calculation and output
calculation_result = None
if operator == '+':
    calculation_result = first_number + second_number
elif operator == '-':
    calculation_result = first_number - second_number
elif operator == '*':
    calculation_result = first_number * second_number
elif operator == '/':
    calculation_result = first_number / second_number
print(calculation_result)

#Files to submit
# when you are done, name this file as solution_hw.py and upload to Moodle