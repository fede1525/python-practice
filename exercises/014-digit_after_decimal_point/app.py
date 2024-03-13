# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
    integer_num = int(num)
    decimal = num - integer_num
    first_digit = (decimal * 10)
    return first_digit


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(23.52))
