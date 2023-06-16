import random

# Generate a random number between 0 and 10 (inclusive)
number = random.randint(0, 10)

# Set the threshold value
threshold = 5

# Check if the number is greater than 8
if number > 8:
    print("big number")   # Print "big number"
    print("big number")   # Print "big number"
    print("big number")   # Print "big number"


# Check if the number is greater than the threshold
elif number > threshold:
    print("very big number")  # Print "very big number"

# Check if the number is less than the threshold
elif number < threshold:
    print("small number")   # Print "small number"

# Check if the number is equal to the threshold
elif number == threshold:
    print("number equal", threshold)   # Print "number equal" followed by the value of the threshold

# Check if the number is greater than 4
if number > 4:
    print('number is greater than 4')  # Print "number is greater than 4"

# Print the generated number
print(number)
