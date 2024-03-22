import re

def valid_password(password):
    pattern = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@])[A-Za-z\d@$#]{6,12}"

    if re.search(pattern, password):
        return "Valid password"
    else:
        return "Invalid password. Please try again"

print(valid_password("asdf24"))
