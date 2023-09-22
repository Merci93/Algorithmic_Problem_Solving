"""A function that adds the elements of an array."""

def add_values(array: list) -> int|float:
    """
    Sum values in an array.
    If item in the array is not an integer or float, it skips this item and proceeds.

    :param array: an array whose elements are to be added.
    :return: result
    """
    try:
        assert type(array) == list
        assert len(array) != 0
        
        total_sum = 0
        for value in array:
            if (type(value) == int or type(value) == float):
                total_sum += value
        return total_sum
    
    except AssertionError:
        print("Not an array or array is empty.")


print(add_values([1, 2, "check", 2, 2.5]))
