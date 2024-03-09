# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    first_digit = 0
    second_digit = 0
    if num > 9:
        first_digit = num / 10
        second_digit = num % 10
    return first_digit, second_digit

# Invoke the function with any integer greater than 9
print(last_two_digits(76))
