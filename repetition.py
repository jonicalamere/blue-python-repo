import random

number = random.randint(0,100)
counter = 0

while number != 52:
      number = random.randint(0,100)
      counter = counter + 1 # counter += 1
      
print(counter, number)

#####################################

for i in range(1000):
    if(number == 52):
        continue
    else:
        number = random.randint(0,100)
        
print(i, number)

############################