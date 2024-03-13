# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):
    leap_year = ((k / 4) == 0 and (k// 100 != 0)) or (k//400 == 0)
    days_previous_month = [0, 31, 28 + leap_year, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    day = (k + sum(days_previous_month[:k % 12])) % 7
    return day

# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(252))
