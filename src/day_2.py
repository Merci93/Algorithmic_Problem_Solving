""" Determine the comparison points between two students."""

def comparison_points(a: list, b: list) -> list:
    """
    Compares two lists and assign points.

    :param a: First list
    :param b: Second list
    :return: List containing assigned points.
    """
    try:
        assert isinstance(a, list) and isinstance(b, list)
        assert len(a) == len(b)
        
        a_points = 0
        b_points = 0
        for i in range(len(a)):
            if a[i] > b[i]:
                a_points += 1
            elif a[i] < b[i]:
                b_points += 1
                
        return [a_points, b_points]
                
    except (AssertionError, TypeError):
        print("Error!!!\n1. Argument(s) not a list.\n2. Contains an unsupported data type.\n3. a and b are not equal in length")
    

print(comparison_points([1, 3], [3, 2, 1]) )
    