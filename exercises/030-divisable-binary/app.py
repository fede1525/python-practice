def divisible_binary(number):
    binary_list = number.split(",")
    decimal_list = [int(binary, 2) for binary in binary_list]
    divisible_numbers = [str(num) for num in decimal_list if num % 5 == 0]
    print(",".join(divisible_numbers) or "None")

divisible_binary("0100,0011,1010,1001")

