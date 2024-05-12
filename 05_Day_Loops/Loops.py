
'''
=> for loop decleratation:
for <iter_variable> in <iterable> :
    your code here
        .
        .
        .
=> while :
i = 0   # you should initialize <iter_variable> before while loop
while <condition> :
    your code here
        .
        .
        .
        i += 1    # this is necessary to finish the after n iterations

'''

# looping through collection

names_list = ['omar','ahmed','mona','mostafa','yousef']
index_list = ['first','second','third','fourth','fifth']
i = 0
for name in names_list:
    print(index_list[i].title(),'name in the list is : ',name.title())
    i += 1
print('\n\n')
    
# looping a number of times 
print('for loop using range function ')
colors = ['green','red','yellow','orange','blue']    
for index in range(0,5):
    print(index ,'  ',colors[index])
print('\n\n')

# looping using while
print('while loop')
names_list = ['omar','ahmed','mona','mostafa','yousef']
index = 0
while index < len(names_list):
    if names_list[index][0] == 'm':
        print(f'name in the list start with m : {names_list[index]}')
    index += 1
print('\n\n')    
# using enumerate 
print('for loop using enumerate')

names_list = ['omar','ahmed','mona','mostafa','yousef']
for name in enumerate(names_list):
    print( name )

print('\n\n')    

while True:
    try:
        num = int(input('Enter a positive integer: '))
        if num > 0:
            break
        else:
            print('Please enter a positive integer.')
    except ValueError:
        print('Invalid input. Please enter an integer.')
print(f"You entered: {num}")
    
