import random
import string


def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


password = get_random_string(25)
print(password)
print(password.replace("a", '@'))
print(password.replace("s", '$'))
