import re

def correct_password(password):

    password_checker = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9].*[^A-Za-z0-9])(?!.*(.)\1\1)[A-Za-z0-9^$%@#&*!?]{6,}$')

    return bool(password_checker.match(password))

# Прогоним doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()

