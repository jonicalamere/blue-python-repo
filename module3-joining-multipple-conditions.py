user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchage programme')
else:
    print('Sorry, you do not qualify')
    
    
    
    user_country = input('What is your country? ')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway' : 
    print('You can apply for a Scandinavian student exchage programme')
else:
    print('Sorry, you do not qualify')
    
    
    user_country = input('Where do you come from? ')
if not user_country == 'Germany' :
    print('you are not from Germany!')
else:
    print('you are from Germany')
    
