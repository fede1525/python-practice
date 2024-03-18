def number_of_uppercase(sentence):
    counts = {"UPPERCASE": 0, "LOWERCASE": 0}

    for char in sentence:
        if char.isupper():
            counts["UPPERCASE"] += 1
        elif char.islower():
            counts["LOWERCASE"] += 1
        else:
            pass
    return f"UPPERCASE {counts['UPPERCASE']} LOWERCASE {counts['LOWERCASE']}"

print(number_of_uppercase("Hello World, How are You?"))
    
