def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
        average = sum / len(input_numbers)
        return average
print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

#next code
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')
    
    
    #did not work when I entered this code from the lesson
    def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')
    
get_average([2])

#also generated a syntax error when this code was ran in Cloud9
def is_first_last_equal(number_list):
    if (number_list[0]) == number_list [-1]):
        return True
    else:
        return False
        
def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return 
    if(number_list[0] == number_list [-1]):
        return True
    else:
        return False
        
    print (is_first_last_equal([]))