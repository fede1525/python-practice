def list_and_tuple(*n):
   string_numbers = [str(num) for num in n]
   string_list = string_numbers
   my_tuple = tuple(string_list)

   print(string_list)
   print(my_tuple)

print(list_and_tuple(34, 67, 55, 33, 12, 98))

