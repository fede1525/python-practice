# Complete the function to return the respective number of the century
def century(year):
    century = int ((year / 100) - 1)
    return century


# Invoke the function with any given year
print(century(1845))
