import random
import string


def generate_string(length=10):
    all_symbols = string.ascii_lowercase
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result
