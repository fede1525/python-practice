class DivisibleBySeven:
    def __init__(self, n):
        self.upper_limit = n

    def iterate_divisibles(self):
        for num in range(self.upper_limit + 1):
            if num % 7 == 0:
                yield num

