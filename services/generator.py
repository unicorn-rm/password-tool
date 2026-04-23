import random
import string

def generate_password(length=14):
    chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        "!@#$%^&*()_+-="
    )

    return "".join(random.choice(chars) for _ in range(length))