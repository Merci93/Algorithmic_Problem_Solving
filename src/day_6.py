def calc_factorial(value: int) -> int|str:
    """
    Calculate the factorial of a non-negative number.

    :param value: Non-negative integer.
    :return: Factorial value.
    """
    if value == 0 or value == 1:
        return 1
    elif value > 1:
        return value * calc_factorial(value - 1)
    else:
        return f"{value} is a negative number."
    

print(calc_factorial(10))
