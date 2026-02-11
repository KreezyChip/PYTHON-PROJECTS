''' Comments must be separated by new line or a semicolon(;)'''

import os; ''' Import for clearing the output '''
os.system("cls"); ''' Output above this function will be cleared '''

''' A variable name and a function for accepting user input '''
name = input("Enter your name: ")
age = input("Enter your age: ")

''' Printing with concatination '''
print("Your name is " + name + " and you are " + age + " years old")

''' This is function checks the data type of the variable'''
print(type(age))

''' Conditional statement '''
if int(age) >= 18 and int(age) <= 55:
    print("You are now an adult"); ''' Proper indentation is significant '''
elif int(age) >= 56:
    print("You are too old")
else:
    print("Still a child")


