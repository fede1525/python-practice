def factorial (n):
    aux = n
    result = n
    while(aux > 1):
        result *= (aux - 1)
        aux -= 1

    return result

print(factorial(8))
