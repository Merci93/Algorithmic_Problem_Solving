def check_str(arg_a: str, arg_b: str) -> bool:
    """
    A function to check and return true if the first argument (string) passed in ends with the 2nd argument

    :param arg_a: First argument
    :param arg_b: Second argument
    :return: boolean
    """
    try:
        assert isinstance(arg_a, str) and isinstance(arg_b, str)
        
        if (arg_a[-1] == arg_b[0]) or (arg_a[-2:] == arg_b[:2]) or arg_a.endswith(arg_b):
            return True
        else:
            return False
    
    except AssertionError:
        print("Error!!!\nArgument(s) not a string")
    

print(check_str("boy", "yogurt"))
print(check_str("house", "eliminate"))
