# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
    hundreds = num / 100
    decimals = num / 10
    first_digit = num % 10
    sum = hundreds + decimals + first_digit
    return sum


# Invoke the function with any three-digit number
print(digits_sum(123))
