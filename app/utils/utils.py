

def validate_password(password: str) -> bool:
    """
    Function takes password and validates if it has
    at least 8 characters and at least one integer number.

    Param password: string parameter to validate.
    Return: bool
    """
    return len(password) >= 8 and any(char in password for char in "0123456789")


def generate_random_int(n: int = 6) -> int:
    """
    Function that generates random code made from n integer numbers
    Param n: number of integers
    Return: Five digit integer.
    """
    from random import randrange
    nums = [str(randrange(1, 10)) for _ in range(n)]
    return int(''.join(nums))
