
print('Exercise 1')
a = 2 + 3
print(a)


a=str(a)+'9'
print(a)

a="Hello"
b="World"
add=a+" "+b
print(add)


a=3.5
b=10
result=a+b
total_sum=result/2
print(total_sum)


print(3**3)

a='d'
b='e'
print(a!=b)

print(6%3)
print('\nExercise 2')
list1, list2 = [1, 2], [3, 4]
list3=list1+list2
print(list3)

grades = ['1.0', '2.3', '1.3', '2.3', '3.0', '1.3']
first=grades[:1]
print(first)

grades = ['1.0', '2.3', '1.3', '2.3', '3.0', '1.3']
grades[2]='F'
print(grades)


grades = ['1.0', '2.3', '1.3', '2.3', '3.0', '1.3']
grades[1:5]
print(grades)

#(d)
grades = ['1.0', '2.3', '1.3', '2.3', '3.0', '1.3']
last_three=grades[-3:]
print(last_three)

#(a)
print('\nExercise 3')
animals = ['cow', 'dog', 'fox', 'horse', 'penguin']
animals.append('zebra')
animals

#(b)
animals = ['cow', 'dog', 'fox', 'horse', 'penguin']
animals.insert(3,'eagle')
animals

#(c)
animals = ['cow', 'dog', 'fox', 'horse', 'penguin']
len(animals)
print('\nExercise 4')
principle = int(input("Welcome, user. I am a financial calculator.\nEnter principal amount (EUR): "))
interest_rate = float(input("Enter annual interest rate (%): "))
rate = (interest_rate / 100)
period = float(input("Enter period (years): "))
# total=(rate*principle)*100
formula = input("Should I calculate compound interest (y/n): ")
if formula == "y":
    r = (1 + rate) ** period
    interest = principle * r - principle
    print(interest)

else:
    interest = (principle * rate * period)
    print(interest)