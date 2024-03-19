def square_odd_numbers(string):
    return [int(num) ** 2 for num in string.split(",") if int(num) % 2 != 0]

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))
