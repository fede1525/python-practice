def all_digits_even():
    even_numbers = []
    for num in range(1000, 3001):
        num_str = str(num)

        if all(int(digit) % 2 == 0 for digit in num_str):
            even_numbers.append(num)
    print(",".join(map(str, even_numbers)))

all_digits_even()
