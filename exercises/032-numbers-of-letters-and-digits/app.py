def letters_and_digits(sentence):
    counts = {"letters": 0, "digits": 0}
    for char in sentence:
        if char.isalpha():
            counts["letters"] += 1
        elif char.isdigit():
            counts["digits"] += 1
    result = "\n".join(f"{key} {value}" for key, value in counts.items())
    return result

print(letters_and_digits("hello world! 123"))
