country = input('what country do live in ? ').lower()



## if province == 'Nunavut' or  province == 'Alberta' or province == 'Yukon':
##     tax = .05
if country == 'canada':
    province = input('what province/state do you live in ?').capitalize()
    
    if province in ('Alberta'\
                    ,'Nunavut','Yukon'):
        tax = .05
    elif province == 'Ontario':
        tax = .13
    else:
        tax = .17

else:
    tax = 0

print('tax rate is :'+str(tax))
 
