# you don't have to copy & paste the same code 
# Functions make your code more readable and easier to maintain.
# Always add comments to explain the purpose of your functions.
# Functions must be declared before the line of code where the function is called.
'''

=> define function 
def <function_name>(arguments):
    your code here
        .
        .
        .
    return 
=> call function 
<function_name>(arguments)

'''

# function to calculate the current time 
from datetime import datetime
def current_time(task_name):
    print(f'{task_name} completed at ' ,end = ' ')
    print( datetime.now())
    print()

# import random module to create random number & string module
from random import randint ,sample
import string

def generate_password():
    total = string.ascii_letters + string.digits
    length = 16
    password = ''.join(sample(total,length))
    return 'Password is : '+password


# function to create user id & random password for user
# you can pass parameter to functions also to do some task on it

def user_id(first_name,last_name):
    first_name_initial = first_name[0:3]
    last_name_initial = last_name[0:2]
    user_id = first_name_initial+last_name_initial+str(randint(100,999))
    print(f'User ID : {user_id}')
    print(generate_password())
    current_time('create user id & Password')
    
        
for i in range(0,100):
    print(i)
    print()
current_time('for loop')


# simple program to create user id & print current time of the task

First_name = input('Enter your First name : ')
Last_name = input('Enter your Last name : ')
user_id(First_name,Last_name)

