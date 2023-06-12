user_age = int(input ('What is your age?'))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congradulations, you qualify!')
    
    
    if True:
        print('Condition met')
    if False: 
        print('Condition')
    if 2 == 2:
        print('true')
    if 1 == 2:
        print('true')
    if 2 == 2.0:
        print ('true')
        
        
        
        answer_a = input('Do you like traveling? y/n:')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')