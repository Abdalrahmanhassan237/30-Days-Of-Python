#----------------------------------- basic bill management ---------------------------------------



country = input('Enter your name of your home country : ')
price = input('How much did you pay? ')
price = float(price)
tax = 0
if country.upper() == 'CANADA':
 
    if price >= 1.00 :
        tax = .07
    # add_else
    else:
        tax


print('tax rate is : '+str(tax))

prices = {'tea' : 6 ,'orange juice' : 26 , 'lemon' : 17 , 'mango' : 32 }

choice = input('Do you want any drinks ? ').upper()
if choice == 'YES':
    for key in enumerate(prices.keys()):
        print(key)
    juice = input('Enter Name of the Drink Do You Want :  ')
    if juice in prices.keys():
        amount = prices[juice]
        total_amount = tax + amount
        change = price - total_amount  
        if total_amount <= price:
            print(f'{juice} price is : {amount}')
            print(f'Total price is : {total_amount}')
            # if change == (-1 * change):
            #     print(f'Your change is : {change * -1}')
            # else :  
            print(f'Your change is : {change }')

        else : 
            print(f'total price is : {total_amount}')
            print('you should pay more')
    else :
        print('write valid name !')
    
      
# short if..else
 
    
