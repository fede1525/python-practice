import math

def square_root(n):
    if n < 0:
        return None
    return round(math.sqrt(n), 2)

print(square_root(8))
